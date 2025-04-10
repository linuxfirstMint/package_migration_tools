"""Unit tests for Pydantic models defined in models/management.py.

These tests verify that the PackageManagement and InputPackageManagement
models can correctly accept structured input and provide expected access patterns.
"""

from models.base import VersionRange
from models.management import PackageManagement

DEPENDENCIES_COUNT = 4


def test_create_package_management_instance(output_mock_data: dict) -> None:
    """Ensure PackageManagement can be instantiated and accessed correctly."""
    instance = PackageManagement(**output_mock_data)
    assert instance.apt.package["git"].version == "1:2.25.1-1ubuntu3.1"
    assert len(instance.apt.package["git"].dependencies) == DEPENDENCIES_COUNT


def test_dependency_version_structure(output_mock_data: dict) -> None:
    """Check that a nested dependency uses the correct version type."""
    instance = PackageManagement(**output_mock_data)
    version_info = instance.brew.package["git"].dependencies[0].version
    assert isinstance(version_info, VersionRange)
    assert version_info.range == ">= 1.0"


def test_input_package_management_merge(input_package_data: dict) -> None:
    """Test that mock input data merges correctly into PackageManagement model."""
    instance = PackageManagement(**input_package_data)
    assert "apt" in instance.model_dump()
    assert "brew" in instance.model_dump()
