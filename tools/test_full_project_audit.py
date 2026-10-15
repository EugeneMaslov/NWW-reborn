"""Regression fixtures for faults that a bracket count alone cannot detect."""
from pathlib import Path
import tempfile
import unittest
import zipfile

from full_project_audit import Audit, ScriptError, VFS, get, parse
from hoi4_script import dump, one, parse as content_parse, engine_script_errors


class ScriptTests(unittest.TestCase):
    def test_comments_strings_and_escaped_quotes_do_not_change_brackets(self):
        text = '# } "\nentry = { name = "A { \\"quoted\\" }" list = { 1 2 3 } }'
        doc = parse(text)
        self.assertEqual(get(get(doc, 'entry'), 'name'), 'A { \\"quoted\\" }')

    def test_unclosed_quote_is_not_silently_discarded(self):
        with self.assertRaises(ScriptError) as caught:
            parse('entry = {\n name = "unfinished\n}\n')
        self.assertEqual(caught.exception.line, 2)

    def test_missing_value_and_extra_brace_are_rejected(self):
        for text in ('entry = { name = }', 'entry = 1 }', 'entry = {'):
            with self.subTest(text=text), self.assertRaises(ScriptError):
                parse(text)

    def test_trailing_top_level_token_is_rejected(self):
        with self.assertRaises(ScriptError):
            parse('entry = { } stray_token')

    def test_division_string_survives_repeated_serialization(self):
        # Real NSB create_unit pattern, including a quoted last field.
        text = r'create_unit = { division = "name = \"International Brigade\" division_template = \"International Brigades\"" owner = ROOT }'
        original = content_parse(text)
        for _ in range(5):
            text = dump(content_parse(text))
            self.assertEqual(content_parse(text), original)
            parse(text)
        self.assertTrue(one(one(original, 'create_unit'), 'division').endswith(r'\"'))

    def test_new_interior_quotes_are_escaped_once(self):
        doc = [('name', 'A "quoted" name', '=')]
        rendered = dump(doc)
        self.assertEqual(one(content_parse(rendered), 'name'), r'A \"quoted\" name')
        self.assertEqual(dump(content_parse(rendered)), rendered)

    def test_real_engine_rejections_are_not_accepted_as_valid_tokens(self):
        doc = content_parse('trigger = { political_power > 49 } modifier = { modifier_army_sub_unit_motorized_attack_factor = 0.1 }')
        messages = list(engine_script_errors(doc))
        self.assertEqual(len(messages), 2)
        self.assertTrue(any('has_political_power' in message for message in messages))
        self.assertTrue(any('motorized_attack_factor' in message for message in messages))


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.game, self.mod = self.base / 'game', self.base / 'mod'
        self.game.mkdir()
        self.mod.mkdir()

    def put(self, root, name, value):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding='utf-8-sig')
        return path

    def test_mod_filename_override_replaces_native_definition(self):
        self.put(self.game, 'common/characters/test.txt', 'characters = { OLD = {} }')
        self.put(self.mod, 'common/characters/test.txt', 'characters = { NEW = {} }')
        audit = Audit(self.mod, self.game)
        audit.definitions()
        self.assertEqual(audit.character_ids, {'NEW'})

    def test_dlc_zip_textures_and_case_sensitive_paths_are_resolved(self):
        dlc = self.game / 'dlc/example'
        dlc.mkdir(parents=True)
        with zipfile.ZipFile(dlc / 'content.zip', 'w') as archive:
            archive.writestr('gfx/Portrait.dds', b'DDS fixture')
        audit = Audit(self.mod, self.game)
        audit.asset('gfx/portrait.dds', 'interface/test.gfx', 8)
        self.assertEqual(audit.issues[0].code, 'texture_case')
        self.assertEqual(audit.vfs.read('gfx/Portrait.dds'), b'DDS fixture')

    def test_replace_path_removes_inherited_files(self):
        self.put(self.game, 'events/base.txt', 'country_event = { id = base.1 }')
        self.put(self.mod, 'test.mod', 'replace_path = "events"')
        self.assertEqual(VFS(self.game, self.mod).names('events'), [])

    def test_interface_bom_is_rejected_despite_a_balanced_ast(self):
        self.put(self.mod, 'interface/ideas.gfx', 'spriteTypes = { spriteType = { name = GFX_test texturefile = "gfx/test.dds" } }')
        audit = Audit(self.mod, self.game)
        audit.syntax()
        self.assertIn('interface_bom', {i.code for i in audit.issues})

    def test_static_ideology_ui_does_not_accept_scripted_callbacks(self):
        self.put(self.mod, 'localisation/replace/english/MKN_ideologies_l_english.yml', 'l_english:\n fascism:0 "[GetNwwMknFascismName]"\n')
        audit = Audit(self.mod, self.game)
        audit.localisation()
        self.assertIn('static_ideology_callback', {i.code for i in audit.issues})

    def test_advisor_effects_need_a_country_scope(self):
        self.put(self.mod, 'common/characters/test.txt', '''characters = { MKN_test = {
            advisor = {
                on_add = { add_ideas = MKN_bonus }
                on_remove = { MKN = { remove_ideas = MKN_bonus } }
            }
        } }''')
        audit = Audit(self.mod, self.game)
        audit.syntax()
        self.assertEqual([i.code for i in audit.issues], ['advisor_callback_scope'])

    def test_ai_static_allowed_and_runtime_enable_are_different(self):
        self.put(self.mod, 'common/ai_strategy_plans/test.txt', '''test = {
            allowed = { original_tag = SOV has_focus_tree = SOV_focus }
            enable = { has_focus_tree = SOV_focus }
        }''')
        audit = Audit(self.mod, self.game)
        audit.syntax()
        self.assertEqual([i.code for i in audit.issues], ['ai_allowed_trigger'])

    def test_missing_mkn_template_labels_are_checked_in_both_languages(self):
        self.put(self.mod, 'history/units/MKN_1936.txt', 'division_template = { name = MKN_Povstancheskaya regiments = { infantry = { x = 0 y = 0 } } }')
        audit = Audit(self.mod, self.game)
        audit.definitions()
        audit.content()
        self.assertEqual({i.message for i in audit.issues if i.code == 'missing'}, {'english: MKN_Povstancheskaya', 'russian: MKN_Povstancheskaya'})

    def test_duplicate_focus_ids_do_not_collect_nested_event_ids(self):
        self.put(self.mod, 'common/national_focus/a.txt',
                 'focus_tree = { id = a focus = { id = F cost = 5 x = 0 y = 0 '
                 'completion_reward = { country_event = { id = event.1 } } } }')
        self.put(self.mod, 'common/national_focus/b.txt',
                 'focus_tree = { id = b focus = { id = F cost = 5 x = 0 y = 0 } }')
        audit = Audit(self.mod, self.game)
        audit.definitions()
        self.assertEqual(set(audit.focuses), {'F'})
        self.assertEqual([i.code for i in audit.issues], ['duplicate'])

    def test_cycles_and_asymmetric_exclusions_are_detected(self):
        self.put(self.mod, 'common/national_focus/a.txt', '''focus_tree = {
            id = tree
            focus = { id = A cost = 5 x = 0 y = 0 prerequisite = { focus = B }
                mutually_exclusive = { focus = B } }
            focus = { id = B cost = 5 x = 2 y = 1 prerequisite = { focus = A } }
        }''')
        audit = Audit(self.mod, self.game)
        audit.definitions()
        audit.focus()
        self.assertEqual({i.code for i in audit.issues}, {'cycle', 'exclusion'})

    def test_zero_cost_is_reserved_for_unselectable_event_focuses(self):
        self.put(self.mod, 'common/national_focus/a.txt', '''focus_tree = {
            id = tree
            focus = { id = EVENT_ONLY cost = 0 x = 0 y = 0 available = { always = no } }
            focus = { id = FREE_SELECTABLE cost = 0 x = 2 y = 0 }
        }''')
        audit = Audit(self.mod, self.game)
        audit.definitions()
        audit.focus()
        errors = [i.message for i in audit.issues if i.code == 'grid_or_cost']
        self.assertEqual(errors, ['FREE_SELECTABLE: cost=0'])

    def test_missing_parent_in_selected_tree_is_detected(self):
        self.put(self.mod, 'common/national_focus/a.txt', '''
            focus_tree = { id = tree_a focus = { id = A cost = 5 x = 0 y = 1 prerequisite = { focus = B } } }
            focus_tree = { id = tree_b focus = { id = B cost = 5 x = 0 y = 0 } }
        ''')
        audit = Audit(self.mod, self.game)
        audit.definitions()
        audit.focus()
        self.assertIn('tree_reference', {i.code for i in audit.issues})

    def test_broken_division_escaping_is_detected_even_with_balanced_braces(self):
        # Two backslashes before an interior quote prematurely close the string.
        self.put(self.mod, 'events/test.txt',
                 r'country_event = { id = test.1 immediate = { create_unit = { division = "name = \\"Broken Brigade\\" division_template = \\"Brigades\\"" owner = ROOT } } }')
        audit = Audit(self.mod, self.game)
        audit.syntax()
        self.assertIn('record_scalar', {i.code for i in audit.issues})

    def test_localisation_bom_duplicate_and_colour_errors_are_detected(self):
        self.put(self.mod, 'localisation/english/one_l_english.yml', 'l_english:\n TEST:0 "§YUnclosed"\n')
        self.put(self.mod, 'localisation/english/two_l_english.yml', 'l_english:\n TEST:0 "Other"\n')
        audit = Audit(self.mod, self.game)
        audit.localisation()
        self.assertEqual({i.code for i in audit.issues}, {'duplicate', 'colour'})

    def test_or_branches_are_not_reported_as_contradictory_conjunctions(self):
        allowed = parse('OR = { tag = MKN tag = UKR }')
        self.assertFalse(Audit.contradictions(allowed))
        blocked = parse('tag = MKN NOT = { tag = MKN }')
        self.assertEqual(Audit.contradictions(blocked), {('tag', 'MKN')})


if __name__ == '__main__':
    unittest.main()
