"""Exposes core models for package management (APT & Homebrew)."""

from .apt import AptPackage
from .base import (
    Dependency,
    VersionExactMatch,
    VersionRange,
    VersionStructCompatible,
    VersionType,
)
from .brew import (
    BrewBottle,
    BrewBottleFile,
    BrewFormula,
    BrewInstalledPackage,
    BrewPackage,
)
from .management import (
    InputPackageManagement,
    Package,
    PackageManagement,
    PackageManager,
)

__all__ = [
    "AptPackage",
    "BrewBottle",
    "BrewBottleFile",
    "BrewFormula",
    "BrewInstalledPackage",
    "BrewPackage",
    "Dependency",
    "InputPackageManagement",
    "Package",
    "PackageManagement",
    "PackageManager",
    "VersionExactMatch",
    "VersionRange",
    "VersionStructCompatible",
    "VersionType",
]
