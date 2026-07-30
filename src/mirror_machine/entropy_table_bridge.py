"""Optional bridge to entropy-table (requires [stack] extra)."""

from __future__ import annotations

from pathlib import Path
from typing import Any


class MirrorMachineBridge:
    """Bridge between MirrorMachine and entropy-table.

    Requires the ``[stack]`` optional dependency group::

        pip install mirror-machine[stack]

    Raises:
        ImportError: if ``entropy-table`` is not installed at all.
        RuntimeError: if ``entropy-table`` is installed but its API no
            longer matches what this bridge expects (see below).
    """

    def __init__(self) -> None:
        from importlib.metadata import PackageNotFoundError
        from importlib.metadata import version as _version

        try:
            _installed_version: str | None = _version("entropy-table")
        except PackageNotFoundError:
            _installed_version = None

        try:
            from entropy_table import EntropyTable  # type: ignore
        except ImportError as exc:
            if _installed_version is None:
                raise ImportError(
                    "entropy-table is required for MirrorMachineBridge. "
                    "Install it with: pip install mirror-machine[stack]"
                ) from exc
            # entropy-table >=2.0 removed the EntropyTable class entirely
            # in favor of a different "contract-first" case/claim-ID data
            # model. This bridge was written against the pre-2.0 API and
            # was never updated, so it previously raised a misleading
            # "not installed" error even when a real, installed
            # entropy-table package was present -- see
            # climate-dashboard-blindtest (same bug, same root cause,
            # found via an ecosystem-wide sweep of sibling bridge files).
            raise RuntimeError(
                f"entropy-table {_installed_version} is installed, but its API no "
                "longer matches what this bridge expects (no EntropyTable class "
                "-- entropy-table >=2.0 replaced the domain-relation model "
                "entirely). This bridge needs updating for the current "
                "entropy-table API; it is not simply a missing dependency."
            ) from exc

        self.table = EntropyTable(domain="mirror-machine")

    def add_reflection(self, key: str, value: Any) -> None:
        """Register a key/value reflection in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export the entropy table to *filepath* (YAML)."""
        self.table.export(filepath)
        return filepath
