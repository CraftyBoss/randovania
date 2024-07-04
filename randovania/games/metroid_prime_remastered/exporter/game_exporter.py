from __future__ import annotations

import dataclasses
import multiprocessing
import subprocess
from concurrent.futures import ProcessPoolExecutor
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any

from randovania.exporter.game_exporter import GameExporter, GameExportParams
from randovania.patching.patchers.exceptions import UnableToExportError

if TYPE_CHECKING:
    from randovania.lib import status_update_lib


class MP1RModPlatform(Enum):
    RYUJINX = "ryujinx"
    ATMOSPHERE = "atmosphere"


@dataclasses.dataclass(frozen=True)
class MP1RGameExportParams(GameExportParams):
    input_path: Path
    output_path: Path


class MP1RGameExporter(GameExporter):
    _busy: bool = False

    @property
    def is_busy(self) -> bool:
        """
        Checks if the exporter is busy right now
        """
        return self._busy

    @property
    def export_can_be_aborted(self) -> bool:
        """
        Checks if export_game can be aborted
        """
        return False

    def export_params_type(self) -> type[GameExportParams]:
        """
        Returns the type of the GameExportParams expected by this exporter.
        """
        return MP1RGameExportParams

    def _do_export_game(
        self,
        patch_data: dict,
        export_params: GameExportParams,
        progress_update: status_update_lib.ProgressUpdateCallable,
    ) -> None:
        assert isinstance(export_params, MP1RGameExportParams)

        # Check if dotnet is available
        dotnet_ran_fine = False
        try:
            dotnet_process = subprocess.run(["dotnet", "--info"], check=False)
            dotnet_ran_fine = dotnet_process.returncode == 0
        except FileNotFoundError:
            dotnet_ran_fine = False
        if not dotnet_ran_fine:
            raise UnableToExportError(
                "You do not have .NET installed!\n"
                "Please ensure that it is installed and located in PATH. It can be installed "
                "from here:\n"
                "https://aka.ms/dotnet/download"
            )

        receiving_pipe, output_pipe = multiprocessing.Pipe(True)

        def on_done(_: Any) -> None:
            output_pipe.send(None)

        with ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit(_run_patcher, patch_data, export_params)
            future.add_done_callback(on_done)
            while not future.done():
                result = receiving_pipe.recv()
                if result is None:
                    break
                message, progress = result
                if message is not None:
                    try:
                        progress_update(message, progress)
                    except Exception:
                        # This should only get triggered when user wants to cancel exporting.
                        # Cancelling is currently broken and thus disabled. If it gets fixed, then this should be
                        # revisited and a test case should be written for this.
                        receiving_pipe.send("close")
                        raise
            future.result()


def _run_patcher(patch_data: dict, export_params: MP1RGameExportParams) -> None:
    from randovania.games.metroid_prime_remastered.exporter.wrapper.wrapper import load_dotnet

    with load_dotnet() as wrapper:
        wrapper.patch(patch_data, export_params.input_path, export_params.output_path)
