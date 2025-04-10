"""Public API entry point for parsing package manager outputs."""

from .apt import parse_apt_output
from .brew import parse_brew_output

__all__ = [
    "parse_apt_output",
    "parse_brew_output",
]
