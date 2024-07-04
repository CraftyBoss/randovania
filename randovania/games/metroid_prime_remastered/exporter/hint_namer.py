from __future__ import annotations

from randovania.games.common.prime_family.exporter.hint_namer import PrimeFamilyHintNamer


class MP1RHintNamer(PrimeFamilyHintNamer):
    def format_temple_name(self, temple_name: str) -> str:
        raise RuntimeError("Not supported")

    def colorize_text(self, color: str, text: str, with_color: bool):
        if with_color:
            return f"<Color={color}>{text}</Color>"
        else:
            return text

    @property
    def color_joke(self) -> str:
        return "#45F731"

    @property
    def color_item(self) -> str:
        return "#c300ff"

    @property
    def color_player(self) -> str:
        return "#d4cc33"

    @property
    def color_location(self) -> str:
        return "#89a1ff"
