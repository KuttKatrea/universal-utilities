import click
import json
import os.path
from subprocess import run

UTF_8 = "utf-8"


@click.command()
def main():
    result = run(["poetry", "env", "info", "-p"], capture_output=True)
    out = result.stdout.decode("utf-8").strip()

    venvPath = os.path.dirname(out)
    venv = os.path.basename(out)

    print(out)
    print(venvPath)
    print(venv)

    version_result = run(
        [
            "poetry",
            "run",
            "python",
            "-c",
            "import sys; print('.'.join([str(s) for s in sys.version_info[:2]]))",
        ],
        capture_output=True,
    )
    version_out = version_result.stdout.decode(UTF_8).strip()

    print(version_out)

    out_filename = "pyrightconf.json"

    with open(out_filename, mode="w", encoding=UTF_8) as fp:
        json.dump(
            {
                "pythonVersion": version_out,
                "venvPath": venvPath,
                "venv": venv,
            },
            fp=fp,
            indent=2,
        )


if __name__ == "__main__":
    main()
