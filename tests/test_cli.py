"""Tests for mirror_machine.cli."""

from typer.testing import CliRunner

from mirror_machine.cli import app

runner = CliRunner()


def test_phase_transition_runs():
    result = runner.invoke(app, ["phase-transition"])
    assert result.exit_code == 0
    assert "Phase transition peak:" in result.output


def test_phase_transition_custom_beta():
    result = runner.invoke(app, ["phase-transition", "--beta", "1.0"])
    assert result.exit_code == 0
    assert "beta=1.0" in result.output


def test_phase_transition_custom_steps():
    result = runner.invoke(app, ["phase-transition", "--steps", "50"])
    assert result.exit_code == 0
    assert "steps=50" in result.output


def test_reflect_missing_file():
    result = runner.invoke(app, ["reflect", "--sigil", "nonexistent.yaml"])
    assert result.exit_code != 0


def test_reflect_valid_sigil(tmp_path):
    sigil = tmp_path / "codex.yaml"
    sigil.write_text("coherence: 1.0\n")
    result = runner.invoke(app, ["reflect", "--sigil", str(sigil)])
    assert result.exit_code == 0
    assert "Mirror reflection complete" in result.output
