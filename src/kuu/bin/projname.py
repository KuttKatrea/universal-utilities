import click
import os
import json
import secrets as random

from click.exceptions import ClickException

consonants = ["", "b", "br", "bl", "c", "ch", "cl", "cr", "d", "dl", "dr", "f", "g", "h", "j", "k", "l", "m", "n", "p", "pr", "pl", "qu", "r", "s", "t", "tr", "tl", "v", "w", "w", "x", "y", "z"]
vocals = ["a", "e", "i", "o", "u"]

forbidden = [
    "qua",
    "quo",
    "quu"
]

valid_sylabbes = [
    i + j
    for i in consonants
    for j in vocals
    if i +j not in forbidden
]

def get_count(maxsylcount):
    return 2 + random.randbelow(maxsylcount - 1)

@click.command()
@click.argument(
    "count",
    default=5
)
@click.argument(
    "maxsylcount",
    default=6
)
def main(count: int, maxsylcount: int):
    for i in range(count):
        parts = [
            random.choice(valid_sylabbes) for i in range(get_count(maxsylcount))
        ]
        click.secho("".join(parts))


if __name__ == "__main__":
    main()

