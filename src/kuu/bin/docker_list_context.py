import click
from subprocess import run

UTF_8 = "utf-8"

DOCKERFILE_CONTENT = """
FROM busybox

WORKDIR /context/
COPY . /context/

RUN find /context/
"""


@click.command()
def main():
    run(
        "docker build -t context-ls -f- .".split(" "),
        input=DOCKERFILE_CONTENT,
        encoding=UTF_8,
        check=True,
    )


if __name__ == "__main__":
    main()
