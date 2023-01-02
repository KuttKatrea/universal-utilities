import click
import os
import json
from subprocess import run

from click.exceptions import ClickException

SUBLIME_PROJECT_EXTENSION = ".sublime-project"
UTF_8 = "utf-8"


def get_default_filename():
    base = os.path.basename(os.getcwd())
    return f"{base}.local"


@click.command()
@click.argument(
    "filename",
    default=get_default_filename,
    type=click.Path(exists=False, dir_okay=False, resolve_path=True, writable=True),
)
def main(filename: str):
    if not filename.endswith(SUBLIME_PROJECT_EXTENSION):
        filename = filename + SUBLIME_PROJECT_EXTENSION

    if os.path.exists(filename):
        run(["subl", filename])
        return

    with open(filename, mode="w", encoding=UTF_8) as fp:
        json.dump(
            {"folders": [{"path": "."}], "settings": {"remember_open_files": True}},
            fp=fp,
            indent=2,
        )

    click.secho(f"Created sublime project file: {filename}")

    run(["subl", filename])


if __name__ == "__main__":
    main()
