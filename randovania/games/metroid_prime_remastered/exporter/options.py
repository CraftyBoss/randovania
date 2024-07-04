from __future__ import annotations

import dataclasses
from pathlib import Path
from typing import Self

from randovania.games.dread.exporter.game_exporter import LinuxRyujinxPath
from randovania.games.game import RandovaniaGame
from randovania.games.metroid_prime_remastered.exporter.game_exporter import MP1RModPlatform
from randovania.interface_common.options import PerGameOptions, decode_if_not_none


@dataclasses.dataclass(frozen=True)
class MP1RPerGameOptions(PerGameOptions):
    """General Options used for Metroid Prime: Remastered."""

    input_path: Path | None = None
    target_platform: MP1RModPlatform = MP1RModPlatform.RYUJINX
    linux_ryujinx_path: LinuxRyujinxPath = LinuxRyujinxPath.FLATPAK
    output_preference: str | None = None

    @property
    def as_json(self) -> dict:
        return {
            **super().as_json,
            "input_path": str(self.input_path) if self.input_path is not None else None,
            "target_platform": self.target_platform.value,
            "linux_ryujinx_path": self.linux_ryujinx_path.value,
            "output_preference": self.output_preference,
        }

    @classmethod
    def from_json(cls, value: dict) -> Self:
        game = RandovaniaGame.METROID_PRIME_REMASTERED
        cosmetic_patches = game.data.layout.cosmetic_patches.from_json(value["cosmetic_patches"])
        return cls(
            cosmetic_patches=cosmetic_patches,
            input_path=decode_if_not_none(value["input_path"], Path),
            target_platform=MP1RModPlatform(value["target_platform"]),
            linux_ryujinx_path=LinuxRyujinxPath(value["linux_ryujinx_path"]),
            output_preference=value["output_preference"],
        )
