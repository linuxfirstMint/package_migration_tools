"""Parsers for transforming dpkg-query output into AptPackage models."""

from models.apt import AptPackage


def parse_apt_output(output: str) -> list[AptPackage]:
    """Parse dpkg-query output into a list of AptPackage models.

    Each line is expected in the format:
        Package=<name>,Version=<version>,Depends=<dep1>, <dep2>, ...

    Args:
        output (str): Multiline string output from `dpkg-query`.

    Returns:
        List[AptPackage]: List of parsed and validated AptPackage models.

    """
    packages = []

    for line in output.strip().splitlines():
        fields = line.strip().split(",")
        parsed = {}
        current_key = None

        for part in fields:
            if "=" in part:
                key, value = part.split("=", 1)
                current_key = key.strip()
                parsed[current_key] = value.strip()
            elif current_key:
                parsed[current_key] += f", {part.strip()}"

        depends_str = parsed.get("Depends", "")
        parsed["Depends"] = (
            [dep.strip() for dep in depends_str.split(",")] if depends_str else []
        )

        packages.append(AptPackage(**parsed))

    return packages
