#!/usr/bin/env python3
"""Generate the MKN Ukrainian Frontier's deterministic, alpha-safe GUI textures.

Uses only Pillow drawing primitives. PNG masters and uncompressed RGBA DDS files
are kept together so the shipped textures can be inspected or regenerated without
an external asset service. Run from any working directory; paths are project bound.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SCALE = 4
SEGMENT_COLORS = (
    (51, 123, 78),
    (140, 172, 58),
    (223, 184, 54),
    (211, 115, 42),
    (154, 43, 56),
)
FOCUS_VARIANTS = {
    "MKN_ukrainian_frontier_root": "frontier",
    "MKN_tachanka_deep_recon": "recon",
    "MKN_donbas_miners_agitation": "miners",
    "MKN_right_of_first_shot": "aim",
    "MKN_armored_train_interceptors": "train",
    "MKN_dnieper_trenches": "fort",
    "MKN_conclude_total_war": "war",
    "MKN_conclude_kharkiv_treaty": "pact",
}


def canvas(size: tuple[int, int]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGBA", (size[0] * SCALE, size[1] * SCALE))
    return image, ImageDraw.Draw(image)


def points(values: list[tuple[float, float]]) -> list[tuple[int, int]]:
    return [(round(x * SCALE), round(y * SCALE)) for x, y in values]


def box(values: tuple[float, float, float, float]) -> tuple[int, int, int, int]:
    return tuple(round(value * SCALE) for value in values)


def finish(image: Image.Image, clearance: int = 1) -> Image.Image:
    image = image.resize(
        (image.width // SCALE, image.height // SCALE), Image.Resampling.LANCZOS
    )
    # Lanczos and glow have a faint fringe; explicitly preserve transparent edges.
    edge = ImageDraw.Draw(image)
    edge.rectangle((0, 0, image.width - 1, clearance - 1), fill=(0, 0, 0, 0))
    edge.rectangle((0, image.height - clearance, image.width - 1, image.height - 1), fill=(0, 0, 0, 0))
    edge.rectangle((0, 0, clearance - 1, image.height - 1), fill=(0, 0, 0, 0))
    edge.rectangle((image.width - clearance, 0, image.width - 1, image.height - 1), fill=(0, 0, 0, 0))
    return image


def make_meter() -> Image.Image:
    image, draw = canvas((400, 36))
    draw.rounded_rectangle(
        box((2, 2, 398, 34)), radius=5 * SCALE,
        fill=(14, 18, 19, 240), outline=(146, 136, 104, 255), width=SCALE,
    )
    font = ImageFont.load_default(size=15 * SCALE)
    for level, color in enumerate(SEGMENT_COLORS, start=1):
        x = 8 + (level - 1) * 78
        draw.rectangle(box((x, 7, x + 75, 29)), fill=(*color, 255))
        draw.line(points([(x, 7), (x + 75, 7)]), fill=(229, 213, 166, 170), width=SCALE)
        draw.line(points([(x, 29), (x + 75, 29)]), fill=(0, 0, 0, 125), width=SCALE)
        draw.text((round((x + 38) * SCALE), 19 * SCALE), str(level),
                  font=font, anchor="mm", fill=(248, 237, 199, 255),
                  stroke_width=SCALE, stroke_fill=(19, 24, 24, 230))
    return finish(image)


def make_emblem() -> Image.Image:
    image, draw = canvas((64, 64))
    gold = (194, 172, 119, 255)
    draw.ellipse(box((3, 3, 61, 61)), fill=(22, 27, 27, 245), outline=gold, width=SCALE)
    draw.ellipse(box((6, 6, 58, 58)), outline=(96, 94, 73, 255), width=SCALE)
    # Railway sleepers and converging steel rails anchor the crossed sabres.
    for y in (27, 34, 42, 51):
        half_width = 7 + (y - 25) * 0.36
        draw.line(points([(32 - half_width, y), (32 + half_width, y)]),
                  fill=(121, 99, 63, 255), width=3 * SCALE)
    for rail in ([25, 20], [39, 44]):
        draw.line(points([(rail[0], 20), (rail[1], 55)]),
                  fill=(19, 20, 18, 255), width=5 * SCALE)
        draw.line(points([(rail[0], 20), (rail[1], 55)]),
                  fill=(151, 157, 149, 255), width=2 * SCALE)
    # One gently curved sabre blade, mirrored for a deliberate crossed emblem.
    blade = [(14, 15), (21, 18), (28, 26), (40, 41), (38, 43),
             (27, 29), (19, 22), (13, 21), (10, 15)]
    for mirrored in (False, True):
        reflect = lambda p: (64 - p[0], p[1]) if mirrored else p
        draw.polygon(points([reflect(p) for p in blade]), fill=(206, 211, 203, 255))
        draw.line(points([reflect((14, 17)), reflect((21, 20)), reflect((39, 41))]),
                  fill=(250, 247, 215, 255), width=SCALE)
        draw.line(points([reflect((36, 43)), reflect((43, 38))]), fill=gold, width=3 * SCALE)
        draw.line(points([reflect((40, 44)), reflect((46, 51))]),
                  fill=(43, 42, 32, 255), width=4 * SCALE)
        draw.line(points([reflect((40, 44)), reflect((46, 51))]),
                  fill=gold, width=SCALE)
        draw.ellipse(box((44 if not mirrored else 16, 49, 49 if not mirrored else 21, 54)),
                     fill=gold)
    # Three wheat-gold studs preserve readability at native category size.
    for x in (26, 32, 38):
        draw.ellipse(box((x - 1, 10, x + 1, 12)), fill=gold)
    return finish(image)


def make_marker() -> Image.Image:
    image, draw = canvas((32, 48))
    arrow = [(10, 6), (22, 6), (22, 14), (27, 14), (16, 25), (5, 14), (10, 14)]
    draw.polygon(points(arrow), fill=(255, 201, 87, 165))
    glow = image.filter(ImageFilter.GaussianBlur(3 * SCALE))
    image = Image.alpha_composite(glow, image)
    draw = ImageDraw.Draw(image)
    draw.polygon(points(arrow), fill=(252, 225, 154, 255),
                 outline=(111, 76, 32, 255), width=SCALE)
    return finish(image)


def make_focus(variant: str) -> Image.Image:
    image, draw = canvas((96, 96))
    gold = (206, 177, 111, 255)
    pale = (235, 218, 172, 255)
    steel = (174, 186, 178, 255)
    shadow = (20, 25, 25, 255)
    red = (178, 66, 55, 255)
    draw.ellipse(box((11, 11, 85, 85)), fill=shadow, outline=gold, width=2 * SCALE)
    draw.ellipse(box((15, 15, 81, 81)), outline=(89, 91, 73, 255), width=SCALE)
    # Symmetrical laurel rim, subdued enough to keep each glyph distinct.
    for mirrored in (False, True):
        for angle in range(-70, 71, 28):
            theta = math.radians(angle)
            x = 48 + (37 if mirrored else -37) * math.cos(theta)
            y = 48 + 37 * math.sin(theta)
            draw.ellipse(box((x - 2, y - 4, x + 2, y + 4)), fill=(141, 139, 91, 255))

    if variant == "frontier":
        emblem = make_emblem().resize((64 * SCALE, 64 * SCALE), Image.Resampling.LANCZOS)
        image.alpha_composite(emblem, (16 * SCALE, 16 * SCALE))
    elif variant == "recon":
        draw.ellipse(box((27, 25, 61, 59)), fill=(42, 66, 61, 255), outline=steel, width=4 * SCALE)
        draw.line(points([(58, 56), (73, 73)]), fill=gold, width=8 * SCALE)
        draw.line(points([(32, 33), (53, 52)]), fill=(111, 139, 127, 255), width=2 * SCALE)
        draw.line(points([(33, 49), (53, 33)]), fill=pale, width=2 * SCALE)
        draw.polygon(points([(33, 47), (32, 38), (41, 47)]), fill=pale)
    elif variant == "miners":
        for mirrored in (False, True):
            reflect = lambda p: (96 - p[0], p[1]) if mirrored else p
            draw.line(points([reflect((31, 67)), reflect((61, 29))]), fill=gold, width=5 * SCALE)
            draw.line(points([reflect((49, 27)), reflect((60, 28)), reflect((70, 39))]),
                      fill=steel, width=5 * SCALE)
        draw.rounded_rectangle(box((39, 51, 57, 70)), radius=3 * SCALE,
                               fill=(75, 63, 37, 255), outline=pale, width=2 * SCALE)
        draw.ellipse(box((44, 55, 52, 65)), fill=(250, 208, 85, 255))
    elif variant == "aim":
        for inset in (0, 9, 18):
            draw.ellipse(box((25 + inset, 25 + inset, 71 - inset, 71 - inset)),
                         outline=steel, width=2 * SCALE)
        draw.line(points([(19, 48), (76, 48)]), fill=gold, width=2 * SCALE)
        draw.line(points([(48, 19), (48, 76)]), fill=gold, width=2 * SCALE)
        draw.ellipse(box((44, 44, 52, 52)), fill=red)
    elif variant == "train":
        for y in (65, 72, 78):
            draw.line(points([(24, y), (72, y)]), fill=(121, 99, 63, 255), width=3 * SCALE)
        for x in (33, 63):
            draw.line(points([(x, 60), (x - 3 if x < 48 else x + 3, 80)]), fill=steel, width=2 * SCALE)
        draw.rectangle(box((32, 30, 64, 51)), fill=(94, 116, 99, 255), outline=pale, width=2 * SCALE)
        draw.rectangle(box((27, 48, 69, 68)), fill=(63, 87, 76, 255), outline=steel, width=2 * SCALE)
        draw.rectangle(box((38, 33, 58, 43)), fill=shadow, outline=gold, width=SCALE)
        draw.polygon(points([(27, 66), (69, 66), (76, 73), (20, 73)]), fill=steel)
        draw.line(points([(48, 22), (48, 32)]), fill=pale, width=4 * SCALE)
        draw.line(points([(48, 25), (68, 25)]), fill=pale, width=3 * SCALE)
        draw.ellipse(box((43, 53, 53, 63)), fill=(245, 218, 127, 255))
    elif variant == "fort":
        draw.polygon(points([(24, 70), (24, 39), (32, 39), (32, 30), (41, 30),
                             (41, 39), (55, 39), (55, 30), (64, 30), (64, 39),
                             (72, 39), (72, 70)]), fill=(120, 123, 110, 255), outline=pale, width=2 * SCALE)
        for y in (46, 54, 62):
            draw.line(points([(26, y), (70, y)]), fill=(59, 71, 62, 255), width=SCALE)
            for x in (34, 48, 62):
                draw.line(points([(x, y), (x, y + 7)]), fill=(59, 71, 62, 255), width=SCALE)
        draw.rectangle(box((42, 50, 54, 70)), fill=shadow, outline=gold, width=SCALE)
    elif variant == "war":
        draw.line(points([(33, 23), (33, 76)]), fill=steel, width=3 * SCALE)
        draw.polygon(points([(34, 24), (51, 19), (73, 25), (69, 49), (52, 43), (34, 48)]),
                     fill=(15, 16, 16, 255), outline=pale, width=SCALE)
        draw.line(points([(41, 65), (66, 45)]), fill=steel, width=4 * SCALE)
        draw.line(points([(44, 44), (68, 66)]), fill=steel, width=4 * SCALE)
        draw.ellipse(box((48, 27, 60, 39)), fill=pale)
        draw.rectangle(box((51, 35, 57, 42)), fill=pale)
        draw.ellipse(box((50, 30, 53, 33)), fill=shadow)
        draw.ellipse(box((56, 30, 59, 33)), fill=shadow)
        draw.polygon(points([(27, 73), (39, 70), (51, 76), (65, 72), (74, 77), (23, 77)]), fill=red)
    elif variant == "pact":
        draw.rounded_rectangle(box((25, 26, 67, 69)), radius=3 * SCALE,
                               fill=(190, 172, 129, 255), outline=pale, width=2 * SCALE)
        draw.ellipse(box((24, 23, 35, 34)), fill=pale, outline=gold, width=SCALE)
        draw.ellipse(box((60, 63, 72, 74)), fill=pale, outline=gold, width=SCALE)
        for y in (37, 43, 49):
            draw.line(points([(34, y), (58, y)]), fill=(91, 89, 67, 255), width=SCALE)
        draw.line(points([(45, 64), (70, 35)]), fill=steel, width=3 * SCALE)
        draw.polygon(points([(66, 33), (78, 24), (75, 40), (63, 42)]), fill=(71, 101, 80, 255))
        draw.ellipse(box((32, 53, 44, 65)), fill=red)
        draw.line(points([(36, 58), (39, 61), (42, 56)]), fill=pale, width=SCALE)
    else:
        raise ValueError(f"Unknown focus glyph: {variant}")
    return finish(image, clearance=5)


def write_focus_sprites() -> None:
    parts = ["# Generated by tools/generate_frontier_gui_assets.py; native goals_shine.gfx pattern.\n",
             "spriteTypes = {\n"]
    for focus_id in FOCUS_VARIANTS:
        texture = f"gfx/interface/frontier_conflicts/focus_{focus_id}.dds"
        parts.append(f'\tspriteType = {{\n\t\tname = GFX_focus_{focus_id}\n\t\ttexturefile = "{texture}"\n\t}}\n')
        parts.append(f'\tspriteType = {{\n\t\tname = GFX_focus_{focus_id}_shine\n'
                     f'\t\ttexturefile = "{texture}"\n\t\teffectFile = "gfx/FX/buttonstate.lua"\n')
        for rotation in (-90.0, 90.0):
            parts.append(f'\t\tanimation = {{\n\t\t\tanimationmaskfile = "{texture}"\n'
                         '\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n'
                         f'\t\t\tanimationrotation = {rotation}\n'
                         '\t\t\tanimationlooping = no\n\t\t\tanimationtime = 0.75\n'
                         '\t\t\tanimationdelay = 0\n\t\t\tanimationblendmode = "add"\n'
                         '\t\t\tanimationtype = "scrolling"\n'
                         '\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n'
                         '\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n\t\t}\n')
        parts.append("\t\tlegacy_lazy_load = no\n\t}\n")
    parts.append("}\n")
    (ROOT / "interface/MKN_frontier_focus_icons.gfx").write_text("".join(parts), encoding="utf-8")


def write_preview(textures: dict[str, Image.Image]) -> None:
    image = Image.new("RGB", (768, 450), (30, 36, 35))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=18)
    draw.text((24, 20), "MKN / UKRAINIAN FRONTIER", font=font, fill=(235, 218, 172))
    image.paste(textures["frontier_escalation_meter"], (122, 75), textures["frontier_escalation_meter"])
    image.paste(textures["icon_frontier_ukr"], (36, 61), textures["icon_frontier_ukr"])
    image.paste(textures["frontier_stage_marker"], (308, 61), textures["frontier_stage_marker"])
    for index, (focus_id, variant) in enumerate(FOCUS_VARIANTS.items()):
        x, y = 44 + (index % 4) * 183, 152 + (index // 4) * 143
        texture = textures[f"focus_{focus_id}"]
        image.paste(texture, (x, y), texture)
        draw.text((x + 48, y + 107), variant.upper(), font=font, anchor="mm", fill=(209, 199, 164))
    preview = ROOT / "docs/art/MKN_frontier_assets_preview.png"
    preview.parent.mkdir(parents=True, exist_ok=True)
    image.save(preview)


def write_texture(folder: Path, stem: str, image: Image.Image) -> None:
    image.save(folder / f"{stem}.png")
    image.save(folder / f"{stem}.dds")
    with Image.open(folder / f"{stem}.dds") as saved:
        decoded = saved.convert("RGBA")
        if decoded.size != image.size or decoded.tobytes() != image.tobytes():
            raise RuntimeError(f"DDS round trip changed {stem}")
    bounds = image.getchannel("A").getbbox()
    if bounds is None:
        raise RuntimeError(f"Empty alpha artwork: {stem}")
    if bounds[0] <= 0 or bounds[1] <= 0 or bounds[2] >= image.width or bounds[3] >= image.height:
        raise RuntimeError(f"Missing transparent edge clearance: {stem}: {bounds}")
    print(f"{stem}: {image.width}x{image.height}, occupied alpha {bounds}, DDS RGBA verified")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "gfx/interface/frontier_conflicts")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    textures = {
        "frontier_escalation_meter": make_meter(),
        "icon_frontier_ukr": make_emblem(),
        "frontier_stage_marker": make_marker(),
        **{f"focus_{focus_id}": make_focus(variant) for focus_id, variant in FOCUS_VARIANTS.items()},
    }
    for stem, image in textures.items():
        write_texture(args.output, stem, image)
    write_focus_sprites()
    write_preview(textures)


if __name__ == "__main__":
    main()
