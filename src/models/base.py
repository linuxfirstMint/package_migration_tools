from pydantic import BaseModel


class VersionRange(BaseModel):
    """Represents a version range constraint for a dependency.

    Example: ">=1.0.0, <2.0.0"
    """

    range: str


class VersionExactMatch(BaseModel):
    """Represents an exact version match requirement.

    Example: "1.2.3"
    """

    exact_match: str


class VersionStructCompatible(BaseModel):
    """Represents compatibility with a version structure.

    Example: "~1.2" would match "1.2.x"
    """

    struct_compatible: str


VersionType = str | VersionRange | VersionExactMatch | VersionStructCompatible


class Dependency(BaseModel):
    """Represents a named dependency with an optional version specification.

    Attributes:
        name (str): Name of the dependent package.
        version (VersionType | None): Optional version constraint.

    """

    name: str
    version: VersionType | None = None
