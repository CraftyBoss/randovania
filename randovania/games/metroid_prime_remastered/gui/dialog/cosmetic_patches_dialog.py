from __future__ import annotations

from typing import TYPE_CHECKING

from randovania.games.metroid_prime_remastered.layout.blank_cosmetic_patches import MP1RCosmeticPatches
from randovania.gui.dialog.base_cosmetic_patches_dialog import BaseCosmeticPatchesDialog
from randovania.gui.generated.blank_cosmetic_patches_dialog_ui import Ui_BlankCosmeticPatchesDialog

if TYPE_CHECKING:
    from PySide6 import QtWidgets

    from randovania.layout.base.cosmetic_patches import BaseCosmeticPatches


class MP1RCosmeticPatchesDialog(BaseCosmeticPatchesDialog, Ui_BlankCosmeticPatchesDialog):
    _cosmetic_patches: MP1RCosmeticPatches

    def __init__(self, parent: QtWidgets.QWidget | None, current: BaseCosmeticPatches):
        super().__init__(parent)
        self.setupUi(self)

        assert isinstance(current, MP1RCosmeticPatches)
        self._cosmetic_patches = current

        self.on_new_cosmetic_patches(current)
        self.connect_signals()

    def connect_signals(self) -> None:
        super().connect_signals()
        # More signals here!

    def on_new_cosmetic_patches(self, patches: MP1RCosmeticPatches) -> None:
        # Update fields with the new values
        pass

    @property
    def cosmetic_patches(self) -> MP1RCosmeticPatches:
        return self._cosmetic_patches

    def reset(self) -> None:
        self.on_new_cosmetic_patches(MP1RCosmeticPatches())
