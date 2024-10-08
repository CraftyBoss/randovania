from __future__ import annotations

import typing

from randovania.games import game
from randovania.games.metroid_prime_remastered import layout
from randovania.layout.preset_describer import GamePresetDescriber

if typing.TYPE_CHECKING:
    from randovania.exporter.game_exporter import GameExporter
    from randovania.exporter.patch_data_factory import PatchDataFactory
    from randovania.interface_common.options import PerGameOptions


def _options() -> type[PerGameOptions]:
    from randovania.games.metroid_prime_remastered.exporter.options import MP1RPerGameOptions

    return MP1RPerGameOptions


def _gui() -> game.GameGui:
    from randovania.games.metroid_prime_remastered import gui

    return game.GameGui(
        game_tab=gui.MP1RGameTabWidget,
        tab_provider=gui.preset_tabs,
        cosmetic_dialog=gui.MP1RCosmeticPatchesDialog,
        export_dialog=gui.MP1RGameExportDialog,
        progressive_item_gui_tuples=(),
        spoiler_visualizer=(),
    )


def _generator() -> game.GameGenerator:
    from randovania.games.metroid_prime_remastered import generator
    from randovania.generator.hint_distributor import AllJokesHintDistributor

    return game.GameGenerator(
        pickup_pool_creator=generator.pool_creator,
        bootstrap=generator.MP1RBootstrap(),
        base_patches_factory=generator.MP1RBasePatchesFactory(),
        hint_distributor=AllJokesHintDistributor(),
    )


def _patch_data_factory() -> type[PatchDataFactory]:
    from randovania.games.metroid_prime_remastered.exporter.patch_data_factory import MP1RPatchDataFactory

    return MP1RPatchDataFactory


def _exporter() -> GameExporter:
    from randovania.games.metroid_prime_remastered.exporter.game_exporter import MP1RGameExporter

    return MP1RGameExporter()


def _hash_words() -> list[str]:
    from randovania.games.metroid_prime_remastered.hash_words import HASH_WORDS

    return HASH_WORDS


game_data: game.GameData = game.GameData(
    short_name="MP1R",
    long_name="Metroid Prime: Remastered",
    development_state=game.DevelopmentState.EXPERIMENTAL,
    presets=[
        {"path": "starter_preset.rdvpreset"},
    ],
    faq=[],
    web_info=game.GameWebInfo(
        what_can_randomize=(
            "Everything",
            "Nothing",
        ),
        need_to_play=(
            "A Hacked Nintendo Switch",
            "A Dump of Metroid Prime: Remastered from a Hacked Switch",
        ),
    ),
    hash_words=_hash_words(),
    layout=game.GameLayout(
        configuration=layout.MP1RConfiguration,
        cosmetic_patches=layout.MP1RCosmeticPatches,
        preset_describer=GamePresetDescriber(),
    ),
    options=_options,
    gui=_gui,
    generator=_generator,
    patch_data_factory=_patch_data_factory,
    exporter=_exporter,
    multiple_start_nodes_per_area=True,
)
