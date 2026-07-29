"""mirror-machine – Theoretical Mirror Framework for the GenesisAeon stack."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

try:
    __version__ = _version("mirror-machine")
except PackageNotFoundError:  # pragma: no cover - not installed, e.g. running from source
    __version__ = "0.0.0+unknown"

__author__ = "GenesisAeon Team"

from .core import MirrorMachine

__all__ = ["MirrorMachine"]
