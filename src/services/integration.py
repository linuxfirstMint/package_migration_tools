"""Integration API for building package management input models."""

from models.management import InputPackageManagement
from parsers import parse_apt_output, parse_brew_output


def build_input_package_management(
    apt_output: str, brew_output: dict
) -> InputPackageManagement:
    """Build InputPackageManagement from raw APT and Brew outputs.

    Args:
        apt_output (str): Raw multiline string from `dpkg-query`.
        brew_output (dict): Parsed JSON output from `brew info --json`.

    Returns:
        InputPackageManagement: Combined and validated model.

    """
    apt_packages = parse_apt_output(apt_output)
    brew_packages = parse_brew_output(brew_output)

    return InputPackageManagement(
        apt_packages=apt_packages,
        brew_packages=brew_packages,
    )
