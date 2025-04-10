"""Pytest fixtures that provide mock package data for unit tests.

These fixtures simulate the output of `dpkg-query` (APT) and `brew info` (Homebrew),
and are used in both parser and model tests.
"""

from typing import Any

import pytest


@pytest.fixture
def output_mock_data() -> dict[str, Any]:
    """Mock data structured for use with the PackageManagement model.

    Returns:
        dict: Nested dict structure simulating parsed package manager data.

    """
    return {
        "apt": {
            "package": {
                "curl": {"version": "7.68.0-1ubuntu2.7", "dependencies": []},
                "git": {
                    "version": "1:2.25.1-1ubuntu3.1",
                    "dependencies": [
                        {"name": "libc6", "version": ">= 2.34"},
                        {"name": "libcurl4", "version": "7.81.0-1ubuntu1.20"},
                        {"name": "zlib1g", "version": ">= 1:1.1.4"},
                        {"name": "zlib2g", "version": ">= 1:1.1.4"},
                    ],
                },
                "wget": {"version": "1.20.3-1ubuntu1", "dependencies": []},
            }
        },
        "brew": {
            "package": {
                "curl": {"version": "8.12.1", "dependencies": []},
                "git": {
                    "version": "2.49.0",
                    "dependencies": [
                        {"name": "libssl", "version": {"range": ">= 1.0"}}
                    ],
                },
                "wget": {"version": "1.25.0", "dependencies": []},
            }
        },
    }


@pytest.fixture
def input_package_data() -> dict[str, Any]:
    """Mock data structured for use with the PackageManagement or integration tests.

    This fixture simulates parsed APT and Brew package input,
    usable as-is for feeding into models expecting dict-style input.

    Returns:
        dict: Dictionary representing mock raw parsed package manager data.

    """
    return {
        "apt": {
            "package": {
                "curl": {"version": "7.81.0-1ubuntu1.20", "dependencies": []},
                "git": {"version": "1:2.34.1-1ubuntu1.12", "dependencies": []},
                "wget": {"version": "1.21.2-2ubuntu1.1", "dependencies": []},
            }
        },
        "brew": {"package": {"git": {"version": "2.48.1", "dependencies": []}}},
    }
