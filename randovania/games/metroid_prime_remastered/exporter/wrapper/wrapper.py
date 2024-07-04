import json
import os
import sys
from contextlib import contextmanager
from pathlib import Path

from pythonnet import load


class PatcherWrapper:
    def __init__(self, lib):
        self.csharp_lib = lib

    def patch(self, patch_data: dict, input_path: Path, output_path: Path):
        self.csharp_lib.Main([input_path.__str__(), output_path.__str__(), json.dumps(patch_data)])


@contextmanager
def load_dotnet() -> PatcherWrapper:
    patcher_path = os.fspath(Path(__file__).with_name(name="patcher"))
    sys.path.append(patcher_path)

    load("coreclr")
    import clr

    clr.AddReference("MP1RRando")
    from MP1RRando import Program as CSharp_Patcher

    try:
        yield PatcherWrapper(CSharp_Patcher)
    except Exception as e:
        raise e
