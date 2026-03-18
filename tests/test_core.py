"""Tests for mirror_machine.core."""

import numpy as np

from mirror_machine.core import MirrorMachine


def test_reflect_loads_sigil(tmp_path):
    sigil = tmp_path / "test.yaml"
    sigil.write_text("coherence: 1.0\ndepth: 3\n")
    mm = MirrorMachine(str(sigil))
    assert "coherence" in mm.state
    assert mm.state["coherence"] == 1.0


def test_reflect_creates_self_reference(tmp_path):
    sigil = tmp_path / "test.yaml"
    sigil.write_text("coherence: 1.0\ndepth: 3\n")
    mm = MirrorMachine(str(sigil))
    assert "reflection" in mm.state
    assert mm.state["reflection"]["coherence"] == 1.0
    assert mm.state["reflection"]["depth"] == 3


def test_reflect_empty_sigil(tmp_path):
    sigil = tmp_path / "empty.yaml"
    sigil.write_text("")
    mm = MirrorMachine(str(sigil))
    assert mm.state == {"reflection": {}}


def test_reflect_via_constructor(tmp_path):
    sigil = tmp_path / "sig.yaml"
    sigil.write_text("key: value\n")
    mm = MirrorMachine(str(sigil))
    assert mm.state["key"] == "value"


def test_reflect_returns_state(tmp_path):
    sigil = tmp_path / "sig.yaml"
    sigil.write_text("x: 42\n")
    mm = MirrorMachine()
    result = mm.reflect(str(sigil))
    assert result is mm.state
    assert result["x"] == 42


def test_phase_transition_shape():
    mm = MirrorMachine()
    result = mm.phase_transition(steps=50)
    assert result.shape == (50,)


def test_phase_transition_default_steps():
    mm = MirrorMachine()
    result = mm.phase_transition()
    assert result.shape == (100,)


def test_phase_transition_is_ndarray():
    mm = MirrorMachine()
    result = mm.phase_transition()
    assert isinstance(result, np.ndarray)


def test_phase_transition_values_positive():
    mm = MirrorMachine()
    result = mm.phase_transition()
    # all values positive: sigmoid > 0 and (1 + φ·sin) >= 1 - 0.618 = 0.382 > 0
    assert result.min() > 0.0
    assert result.max() > 0.0


def test_phase_transition_beta_affects_steepness():
    mm = MirrorMachine()
    steep = mm.phase_transition(beta=2.0)
    gentle = mm.phase_transition(beta=0.01)
    # With steeper beta, the mid-point value is higher earlier; check max difference
    assert not np.allclose(steep, gentle)


def test_no_sigil_on_init():
    mm = MirrorMachine()
    assert mm.state == {}
