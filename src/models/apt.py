from pydantic import BaseModel, Field


class AptPackage(BaseModel):
    """Represents a package entry from APT (Debian-based systems).

    Attributes:
        package (str): The name of the package (e.g., 'curl').
        version (str): The version string of the package.
        depends (list[str]): List of dependency package names as strings.

    """

    package: str = Field(..., alias="Package")
    version: str = Field(..., alias="Version")
    depends: list[str] = Field(..., alias="Depends")
