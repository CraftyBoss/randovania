from __future__ import annotations

import copy
import dataclasses
from typing import TYPE_CHECKING

from randovania.game_description.requirements.resource_requirement import ResourceRequirement
from randovania.games.metroid_prime_remastered.layout.blank_configuration import MP1RConfiguration
from randovania.resolver.bootstrap import MetroidBootstrap

if TYPE_CHECKING:
    from randovania.game_description.resources.resource_database import ResourceDatabase
    from randovania.layout.base.base_configuration import BaseConfiguration


class MP1RBootstrap(MetroidBootstrap):
    def patch_resource_database(self, db: ResourceDatabase, configuration: BaseConfiguration) -> ResourceDatabase:
        assert isinstance(configuration, MP1RConfiguration)

        requirement_template = copy.copy(db.requirement_template)

        suits = [db.get_item_by_name("Varia Suit")]
        if not configuration.legacy_mode:
            requirement_template["Heat-Resisting Suit"] = dataclasses.replace(
                requirement_template["Heat-Resisting Suit"],
                requirement=ResourceRequirement.simple(db.get_item_by_name("Varia Suit")),
            )
        else:
            suits.extend([db.get_item_by_name("Gravity Suit"), db.get_item_by_name("Phazon Suit")])

        return dataclasses.replace(
            db,
            requirement_template=requirement_template,
        )
