"""Integration tests for parser + model workflow.

This test ensures that the output of apt/brew parsers can be correctly
used to construct a valid InputPackageManagement Pydantic model.
"""

from models.management import InputPackageManagement
from parsers import parse_apt_output, parse_brew_output
from services.integration import build_input_package_management


def test_input_package_management_from_parsers(
    input_apt_mock_data: dict[str, any], input_brew_mock_data: dict[str, any]
) -> None:
    """Full integration: mock input -> parsed -> validated model."""
    apt_pkgs = parse_apt_output(input_apt_mock_data)
    brew_pkg = parse_brew_output(input_brew_mock_data)

    instance = InputPackageManagement(
        apt_packages=apt_pkgs,
        brew_packages=brew_pkg,
    )

    assert instance.apt_packages[0].package == "curl"
    assert instance.brew_packages.formulae[0].name == "git"


def test_build_input_package_management(
    input_apt_mock_data: dict[str, any], input_brew_mock_data: dict[str, any]
) -> None:
    """Test that the API builds InputPackageManagement from raw inputs."""
    result = build_input_package_management(input_apt_mock_data, input_brew_mock_data)

    assert result.apt_packages[0].package == "curl"
    assert result.brew_packages.formulae[0].name == "git"
    assert result.brew_packages.formulae[0].versions["stable"] == "2.48.1"
    assert result.brew_packages.formulae[0].bottle is not None
