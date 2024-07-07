from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import randovania
from randovania.exporter import pickup_exporter
from randovania.exporter.hints import credits_spoiler, guaranteed_item_hint
from randovania.exporter.patch_data_factory import PatchDataFactory
from randovania.game_description.assignment import PickupTarget
from randovania.game_description.db.pickup_node import PickupNode
from randovania.games.game import RandovaniaGame
from randovania.games.metroid_prime_remastered.exporter.hint_namer import MP1RHintNamer
from randovania.games.prime1.layout.hint_configuration import ArtifactHintMode
from randovania.games.prime1.patcher import prime1_elevators, prime_items
from randovania.generator.pickup_pool import pickup_creator

if TYPE_CHECKING:
    from randovania.game_description.db.area_identifier import AreaIdentifier
    from randovania.game_description.db.node_identifier import NodeIdentifier
    from randovania.game_description.db.region_list import RegionList
    from randovania.games.metroid_prime_remastered.layout.blank_configuration import MP1RConfiguration
    from randovania.games.metroid_prime_remastered.layout.blank_cosmetic_patches import MP1RCosmeticPatches
    from randovania.layout.layout_description import LayoutDescription


def _remove_empty(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary"""

    def empty(x):
        return x is None or x == {} or x == [] or x == ""

    if not isinstance(d, dict | list):
        return d
    elif isinstance(d, list):
        return [v for v in (_remove_empty(v) for v in d) if not empty(v)]
    else:
        return {k: v for k, v in ((k, _remove_empty(v)) for k, v in d.items()) if not empty(v)}


def prime_remastered_pickup_details_to_patcher(detail: pickup_exporter.ExportedPickupDetails) -> dict:
    name = detail.model.name
    pickup_type = "Nothing"
    count = 0

    if detail.other_player:
        pickup_type = "Unknown Item 1"
        count = detail.index.index + 1
    else:
        for resource, quantity in detail.conditional_resources[0].resources:
            if resource.extra["item_id"] >= 1000:
                continue
            pickup_type = name
            count = quantity
            break

    result = {
        "type": pickup_type,
        # "scanText": f"{name}. {detail.description}".strip(),
        # "hudmemoText": collection_text,
        "pickupCount": count,
    }

    return result


def _name_for_location(region_list: RegionList, location: AreaIdentifier) -> str:
    loc = location.as_tuple
    if loc in prime1_elevators.RANDOMPRIME_CUSTOM_NAMES and loc != ("Frigate Orpheon", "Exterior Docking Hangar"):
        return prime1_elevators.RANDOMPRIME_CUSTOM_NAMES[loc]
    else:
        return region_list.area_name(region_list.area_by_area_location(location), separator=":")


def _name_for_start_location(region_list: RegionList, location: NodeIdentifier) -> str:
    # small helper function as long as teleporter nodes use AreaIdentifier and starting locations use NodeIdentifier
    area_loc = location.area_identifier
    return _name_for_location(region_list, area_loc)


def _create_results_screen_text(description: LayoutDescription) -> str:
    return f"{randovania.VERSION} | Seed Hash - {description.shareable_word_hash} ({description.shareable_hash})"


class MP1RPatchDataFactory(PatchDataFactory):
    cosmetic_patches: MP1RCosmeticPatches
    configuration: MP1RConfiguration

    def game_enum(self) -> RandovaniaGame:
        return RandovaniaGame.METROID_PRIME_REMASTERED

    def create_game_specific_data(self) -> dict:
        # Setup
        db = self.game
        namer = MP1RHintNamer(self.description.all_patches, self.players_config)

        useless_target = PickupTarget(
            pickup_creator.create_nothing_pickup(db.resource_database), self.players_config.player_index
        )

        pickup_list = pickup_exporter.export_all_indices(
            self.patches,
            useless_target,
            db.region_list,
            self.rng,
            self.configuration.pickup_model_style,
            self.configuration.pickup_model_data_source,
            exporter=pickup_exporter.create_pickup_exporter(
                pickup_exporter.GenericAcquiredMemo(), self.players_config, self.game_enum()
            ),
            visual_nothing=pickup_creator.create_visual_nothing(self.game_enum(), "Nothing"),
        )

        regions = [region for region in db.region_list.regions if region.name != "End of Game"]

        # Initialize serialized db data
        level_data = {}
        for region in regions:
            level_data[region.name] = {
                "transports": {},
                "rooms": {},
            }

            for area in region.areas:
                level_data[region.name]["rooms"][area.name] = {
                    "pak_path": "",
                    "pickups": [],
                    "doors": {},
                }

        # serialize pickup modifications
        for region in regions:
            for area in region.areas:
                pickup_nodes = (node for node in area.nodes if isinstance(node, PickupNode))
                pickup_nodes = sorted(pickup_nodes, key=lambda n: n.pickup_index)

                if len(pickup_nodes) > 0:
                    rel_path = Path(region.extra["pak_folder"])
                    rel_path = rel_path.joinpath(area.extra["pak_file"] + ".pak")

                    level_data[region.name]["rooms"][area.name]["pakPath"] = rel_path.__str__()

                for node in pickup_nodes:
                    pickup_index = node.pickup_index.index
                    pickup = prime_remastered_pickup_details_to_patcher(pickup_list[pickup_index])
                    if "instance_id" in node.extra:
                        pickup["instanceId"] = node.extra["instance_id"]
                    else:
                        raise Exception("Missing Instance ID in node! " + node.name + " Area Name: " + area.name)

                    level_data[region.name]["rooms"][area.name]["pickups"].append(pickup)

        # strip extraneous info
        level_data = _remove_empty(level_data)
        for region_item in level_data.values():
            if "rooms" not in region_item:
                region_item["rooms"] = {}

        credits_string = credits_spoiler.prime_trilogy_credits(
            self.configuration.standard_pickup_configuration,
            self.description.all_patches,
            self.players_config,
            namer,
            "<Color=#89D6FF>Major Item Locations</Color>",
            "<Color=#33FFD6>{}</Color>",
        )

        artifacts = [db.resource_database.get_item(index) for index in prime_items.ARTIFACT_ITEMS]
        hint_config = self.configuration.hints
        if hint_config.artifacts == ArtifactHintMode.DISABLED:
            resulting_hints = {art: f"{art.long_name} is lost somewhere on Tallon IV." for art in artifacts}
        else:
            resulting_hints = guaranteed_item_hint.create_guaranteed_hints_for_resources(
                self.description.all_patches,
                self.players_config,
                namer,
                hint_config.artifacts == ArtifactHintMode.HIDE_AREA,
                [db.resource_database.get_item(index) for index in prime_items.ARTIFACT_ITEMS],
                True,
            )

        # Tweaks

        starting_room = _name_for_start_location(db.region_list, self.patches.starting_location)

        starting_resources = self.patches.starting_resources()

        data: dict = {
            # TODO: develop new schema for data
            # "$schema": "https://randovania.github.io/randomprime/randomprime.schema.json",
            "seed": self.description.get_seed_for_player(self.players_config.player_index),
            "gameConfig": {
                "resultsString": _create_results_screen_text(self.description),
                "startingRoom": starting_room,
                "difficultyBehavior": self.configuration.ingame_difficulty.randomprime_value,
                "mainMenuMessage": f"Randovania v{randovania.VERSION}\n{self.description.shareable_word_hash}",
                "creditsString": credits_string,
                "artifactHints": {artifact.long_name: text for artifact, text in resulting_hints.items()},
                "artifactTempleLayerOverrides": {
                    artifact.long_name: not starting_resources.has_resource(artifact) for artifact in artifacts
                },
                "requiredArtifactCount": self.configuration.artifact_required.value,
            },
            "levelData": level_data,
            "hasSpoiler": self.description.has_spoiler,
            "uuid": list(
                self.players_config.get_own_uuid().bytes,
            ),
        }

        return data
