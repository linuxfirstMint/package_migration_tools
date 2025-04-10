from pydantic import BaseModel, Field

from models import AptPackage, BrewPackage, Dependency


class Package(BaseModel):
    """Generic representation of a package (APT or Brew).

    Attributes:
        version (str): Version string.
        dependencies (list[Dependency]): Dependencies with version info.

    """

    version: str
    dependencies: list[Dependency] = Field(default_factory=list)


class PackageManager(BaseModel):
    """A set of named packages managed by a system.

    Attributes:
        package (dict[str, Package]): Mapping of name -> Package object.

    """

    package: dict[str, Package]


class PackageManagement(BaseModel):
    """Top-level structure of packages under multiple managers.

    Attributes:
        apt (PackageManager | None): APT-managed packages.
        brew (PackageManager | None): Homebrew-managed packages.

    """

    apt: PackageManager | None = None
    brew: PackageManager | None = None


class InputPackageManagement(BaseModel):
    """Represents raw package data parsed from command outputs.

    Attributes:
        apt_packages (list[AptPackage]): List of parsed APT packages.
        brew_packages (BrewPackage): Parsed Homebrew data.

    """

    apt_packages: list[AptPackage]
    brew_packages: BrewPackage
