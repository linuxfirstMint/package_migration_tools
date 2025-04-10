from pydantic import BaseModel


class BrewBottleFile(BaseModel):
    """Metadata for a Homebrew bottle file (per platform/arch).

    Attributes:
        cellar (str): Installation location.
        url (str): Download URL.
        sha256 (str): File checksum.

    """

    cellar: str
    url: str
    sha256: str


class BrewBottle(BaseModel):
    """Represents stable bottle info for a Homebrew formula.

    Attributes:
        stable (dict[str, BrewBottleFile]): Map of platform -> bottle file.

    """

    stable: dict[str, BrewBottleFile]


class BrewInstalledPackage(BaseModel):
    """Represents an installed Homebrew package instance.

    Attributes:
        version (str): Installed version.
        installed_as_dependency (bool | None): Installed as dependency?
        runtime_dependencies (list[str] | None): Other runtime dependencies.

    """

    version: str
    installed_as_dependency: bool | None = None
    runtime_dependencies: list[str] | None = None


class BrewFormula(BaseModel):
    """Represents a Homebrew formula entry.

    Attributes:
        name (str): Short name.
        full_name (str): Full tap-qualified name.
        tap (str): Tap source.
        versioned_formulae (list[str]): Other versions.
        desc (str): Description.
        license (str): License.
        homepage (str): URL.
        versions (dict): Version info.
        urls (dict): Download metadata.
        revision (int): Revision number.
        dependencies (list[str]): Dependency package names.
        installed (list[BrewInstalledPackage]): Installed versions.
        bottle (BrewBottle | None): Bottle metadata.

    """

    name: str
    full_name: str
    tap: str
    versioned_formulae: list[str]
    desc: str
    license: str
    homepage: str
    versions: dict[str, str | None]
    urls: dict[str, dict[str, str | None]]
    revision: int
    dependencies: list[str]
    installed: list[BrewInstalledPackage]
    bottle: BrewBottle | None = None


class BrewPackage(BaseModel):
    """Represents a full Homebrew package block.

    Attributes:
        formulae (list[BrewFormula]): Installed formulae.
        casks (list[dict[str, str]]): Installed casks.

    """

    formulae: list[BrewFormula]
    casks: list[dict[str, str]]
