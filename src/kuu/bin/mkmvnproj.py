import click
import json
import os.path
from subprocess import run


@click.command()
@click.argument(
    "group_id",
)
@click.argument(
    "artifact_id",
)
def main(group_id, artifact_id):
    run(
        [
            "mvn",
            "archetype:generate",
            f"-DgroupId={group_id}",
            f"-DartifactId={artifact_id}",
            "-DarchetypeArtifactId=maven-archetype-quickstart",
            "-DarchetypeVersion=1.4",
            "-DinteractiveMode=false",
        ]
    )


if __name__ == "__main__":
    main()
