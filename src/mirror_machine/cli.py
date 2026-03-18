"""Mirror-Machine CLI – self-referential framework commands."""

from __future__ import annotations

import typer
from rich.console import Console

from .core import MirrorMachine

app = typer.Typer(help="Mirror-Machine CLI – self-referential Mirror Framework.")
console = Console()


@app.command()
def reflect(
    sigil: str = typer.Option("codex-prime.yaml", help="Path to sigil YAML file."),
) -> None:
    """Reflect a sigil and display its self-reference."""
    mm = MirrorMachine(sigil)
    console.print("[bold green]Mirror reflection complete[/]")
    console.print(mm.state)


@app.command()
def phase_transition(
    beta: float = typer.Option(0.0625, help="Transition steepness (default: 0.0625)."),
    steps: int = typer.Option(100, help="Number of simulation steps."),
) -> None:
    """Simulate a consciousness phase transition and report the peak."""
    mm = MirrorMachine()
    transition = mm.phase_transition(beta=beta, steps=steps)
    console.print(f"[bold magenta]Phase transition peak:[/] {transition.max():.4f}")
    console.print(f"[dim]beta={beta}  steps={steps}[/]")


if __name__ == "__main__":
    app()
