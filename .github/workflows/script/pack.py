import json
import shutil
from pathlib import Path


def main():
    with Path("version.json").open("r") as f:
        version = json.load(f)["version"]

    shutil.make_archive(
        base_name=f"ZeroDataPack-{version}",
        format="zip",
        root_dir="datapack"
    )


if __name__ == "__main__":
    main()