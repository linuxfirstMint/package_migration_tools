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


@pytest.fixture
def input_apt_mock_data() -> str:
    """APT package list as raw dpkg-query output."""
    return (
        "Package=curl,Version=7.81.0-1ubuntu1.20,Depends=libc6 (>= 2.34), "
        "libcurl4 (= 7.81.0-1ubuntu1.20), zlib1g (>= 1:1.1.4)\n"
        "Package=git,Version=1:2.34.1-1ubuntu1.12,Depends=libc6 (>= 2.34), "
        "libcurl3-gnutls (>= 7.56.1), libexpat1 (>= 2.0.1), libpcre2-8-0 (>= 10.34), "
        "zlib1g (>= 1:1.2.0), perl, liberror-perl, git-man (>> 1:2.34.1), "
        "git-man (<< 1:2.34.1-.)\n"
        "Package=wget,Version=1.21.2-2ubuntu1.1,Depends=libc6 (>= 2.34), "
        "libidn2-0 (>= 0.6), libpcre2-8-0 (>= 10.22), libpsl5 (>= 0.16.0), "
        "libssl3 (>= 3.0.0~~alpha1), libuuid1 (>= 2.16), zlib1g (>= 1:1.1.4)"
    )


@pytest.fixture
def input_brew_mock_data() -> dict:
    """Mock data simulating `brew info --json=v2 <pkg>` format."""
    return {
        "formulae": [
            {
                "name": "git",
                "full_name": "git",
                "tap": "homebrew/core",
                "versioned_formulae": [],
                "desc": "Distributed revision control system",
                "license": "GPL-2.0-only",
                "homepage": "https://git-scm.com",
                "versions": {"stable": "2.48.1", "head": "HEAD", "bottle": "true"},
                "urls": {},
                "revision": 0,
                "dependencies": ["gettext", "pcre2", "openssl@3"],
                "installed": [],
                "bottle": {
                    "stable": {
                        "files": {
                            "x86_64_linux": {
                                "cellar": "/home/linuxbrew/.linuxbrew/Cellar",
                                "url": "https://ghcr.io/v2/homebrew/core/git/blobs/sha256:example",
                                "sha256": "examplehash",
                            }
                        }
                    }
                },
            }
        ],
        "casks": [],
    }
