"""Mirror Principle – self-reflective loops and consciousness phase transitions."""

from __future__ import annotations

from typing import Any

import numpy as np
import yaml


class MirrorMachine:
    """Self-referential Mirror Framework.

    Reflects sigils and simulates consciousness phase transitions.
    """

    def __init__(self, sigil_path: str | None = None) -> None:
        self.state: dict[str, Any] = {}
        if sigil_path:
            self.reflect(sigil_path)

    def reflect(self, sigil_path: str) -> dict[str, Any]:
        """Load and self-reflect a sigil (trilayer YAML).

        Creates a recursive self-reference by mirroring all top-level keys
        into a nested ``reflection`` entry, embodying the Mirror Principle.
        """
        with open(sigil_path) as f:
            data: dict[str, Any] = yaml.safe_load(f) or {}
        self.state = data
        self.state["reflection"] = dict(data)
        return self.state

    def phase_transition(self, beta: float = 0.0625, steps: int = 100) -> np.ndarray:
        """Simulate a consciousness phase transition.

        Uses a sigmoid (logistic) phase shift modulated by a golden-ratio
        oscillation to produce the characteristic mirror-emergence curve.

        Args:
            beta: Transition steepness (default 0.0625 → gentle emergence).
            steps: Number of time steps across [0, 10].

        Returns:
            1-D array of shape ``(steps,)`` with the reflection signal.
        """
        t = np.linspace(0, 10, steps)
        transition = 1 / (1 + np.exp(-beta * (t - 5)))  # sigmoid phase shift
        reflection = transition * (1 + 0.618 * np.sin(t * 2 * np.pi))  # φ oscillation
        return reflection
