"""Compatibility entry point; rebuild presentation without overwriting mechanics."""
from build_austria_presentation import build_icons, build_panel

if __name__ == '__main__':
    build_icons()
    build_panel()
