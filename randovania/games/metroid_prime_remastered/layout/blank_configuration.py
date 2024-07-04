from __future__ import annotations

import dataclasses

from randovania.games.game import RandovaniaGame
from randovania.games.prime1.layout.prime_configuration import (
    EnemyAttributeRandomizer,
    HintConfiguration,
    IngameDifficulty,
    LayoutArtifactMode,
    LayoutCutsceneMode,
    PrimeTrilogyTeleporterConfiguration,
    RoomRandoMode,
)
from randovania.layout.base.base_configuration import BaseConfiguration


@dataclasses.dataclass(frozen=True)
class MP1RConfiguration(BaseConfiguration):
    # TODO: Remove unsupported features
    teleporters: PrimeTrilogyTeleporterConfiguration
    hints: HintConfiguration
    energy_per_tank: int = dataclasses.field(metadata={"min": 1, "max": 1000, "precision": 1})
    artifact_required: LayoutArtifactMode
    artifact_minimum_progression: int = dataclasses.field(metadata={"min": 0, "max": 99})
    heat_damage: float = dataclasses.field(metadata={"min": 0.1, "max": 99.9, "precision": 3.0})
    warp_to_start: bool
    progressive_damage_reduction: bool
    allow_underwater_movement_without_gravity: bool
    small_samus: bool
    large_samus: bool
    shuffle_item_pos: bool
    items_every_room: bool
    random_boss_sizes: bool
    no_doors: bool
    superheated_probability: int = dataclasses.field(
        metadata={"min": 0, "max": 1000}
    )  # div 1000 to get coefficient, div 10 to get %
    submerged_probability: int = dataclasses.field(
        metadata={"min": 0, "max": 1000}
    )  # div 1000 to get coefficient, div 10 to get %
    room_rando: RoomRandoMode
    spring_ball: bool

    main_plaza_door: bool
    blue_save_doors: bool
    backwards_frigate: bool
    backwards_labs: bool
    backwards_upper_mines: bool
    backwards_lower_mines: bool
    phazon_elite_without_dynamo: bool

    legacy_mode: bool
    qol_cutscenes: LayoutCutsceneMode
    ingame_difficulty: IngameDifficulty

    enemy_attributes: EnemyAttributeRandomizer | None

    @classmethod
    def game_enum(cls) -> RandovaniaGame:
        return RandovaniaGame.METROID_PRIME_REMASTERED

    def active_layers(self) -> set[str]:
        layers = {"default"}
        return layers
