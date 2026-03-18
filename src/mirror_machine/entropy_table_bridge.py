"""Optional bridge to entropy-table (requires [stack] extra)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    from entropy_table import EntropyTable  # type: ignore[import-untyped]

    _ENTROPY_TABLE_AVAILABLE = True
except ImportError:
    _ENTROPY_TABLE_AVAILABLE = False


class MirrorMachineBridge:
    """Bridge between MirrorMachine and entropy-table.

    Requires the ``[stack]`` optional dependency group::

        pip install mirror-machine[stack]

    Raises:
        ImportError: if ``entropy-table`` is not installed.
    """

    def __init__(self) -> None:
        if not _ENTROPY_TABLE_AVAILABLE:
            raise ImportError(
                "entropy-table is required for MirrorMachineBridge. "
                "Install it with: pip install mirror-machine[stack]"
            )
        self.table = EntropyTable(domain="mirror-machine")

    def add_reflection(self, key: str, value: Any) -> None:
        """Register a key/value reflection in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export the entropy table to *filepath* (YAML)."""
        self.table.export(filepath)
        return filepath
