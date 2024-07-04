from __future__ import annotations

from typing import TYPE_CHECKING

from randovania.games.metroid_prime_remastered.generator.pickup_pool.artifacts import add_artifacts
from randovania.games.metroid_prime_remastered.layout.blank_configuration import MP1RConfiguration

if TYPE_CHECKING:
    from randovania.game_description.game_description import GameDescription
    from randovania.generator.pickup_pool import PoolResults


def pool_creator(results: PoolResults, configuration: MP1RConfiguration, game: GameDescription):
    assert isinstance(configuration, MP1RConfiguration)
    results.extend_with(
        add_artifacts(
            game.resource_database,
            configuration.artifact_required,
            configuration.artifact_minimum_progression,
        )
    )
