import click
import subprocess
from typing import Optional, cast
import urllib.parse
import sys
import platform
import logging


@click.command()
@click.option("-e", "--executable")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
)
@click.option("-p", "--profile")
@click.option("-c", "--container", required=True)
@click.option("--url", required=True)
def main(
    container: str,
    url: str,
    verbose: bool,
    executable: Optional[str] = None,
    profile: Optional[str] = None,
):
    if not executable:
        executable = get_default_executable()

    command = [executable]
    if profile:
        command.append("-P")
        command.append(profile)

    url = f"ext+container:url={urllib.parse.quote(url)}&name={container}"
    command.append(url)

    if verbose:
        click.secho(f"Running: {command}")

    subprocess.run(command)


def get_default_executable():
    if platform.system() == "Windows":
        try:
            return get_default_executable_from_registry()
        except Exception:
            click.secho(
                "Error getting the firefox executable path from registry.", err=True
            )

        return "firefox.exe"

    return "firefox"


def get_default_executable_from_registry():
    import winreg

    key = winreg.OpenKeyEx(
        winreg.HKEY_CURRENT_USER, "SOFTWARE\\Mozilla\\Mozilla Firefox"
    )
    val, _ = winreg.QueryValueEx(key, "CurrentVersion")
    winreg.CloseKey(key)

    key = winreg.OpenKeyEx(
        winreg.HKEY_CURRENT_USER, f"SOFTWARE\\Mozilla\\Mozilla Firefox\\{val}\\Main"
    )
    val, _ = winreg.QueryValueEx(key, "PathToExe")
    winreg.CloseKey(key)

    return cast(str, val)


if __name__ == "__main__":
    main()
