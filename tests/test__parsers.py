"""Unit tests for APT and Homebrew parser functions.

These tests validate that raw output strings and dictionaries
are correctly parsed into the appropriate Pydantic models.
"""

from models.apt import AptPackage
from models.brew import BrewPackage
from parsers import parse_apt_output, parse_brew_output

PACKAGES_LEN = 3


def test_parse_apt_output(input_apt_mock_data: dict[str, any]) -> None:
    """Test that apt mock output is parsed into AptPackage models."""
    packages = parse_apt_output(input_apt_mock_data)
    assert isinstance(packages, list)
    assert all(isinstance(pkg, AptPackage) for pkg in packages)
    assert len(packages) == PACKAGES_LEN
    assert packages[0].package == "curl"


def test_parse_brew_output(input_brew_mock_data: dict[str, any]) -> None:
    """Test that brew mock output is parsed into BrewPackage."""
    package = parse_brew_output(input_brew_mock_data)
    assert isinstance(package, BrewPackage)
    assert len(package.formulae) == 1
    assert package.formulae[0].name == "git"
