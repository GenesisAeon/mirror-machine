# Mirror Machine

**Theoretical Mirror Framework** – self-referential loops, consciousness phase transitions and Mirror Principle simulation for the GenesisAeon stack.

## Core Concepts

| Concept | Description |
|---|---|
| **Mirror Principle** | A sigil (YAML) is loaded and reflected into itself, creating a self-referential state |
| **Phase Transition** | Sigmoid × golden-ratio (φ) oscillation models consciousness emergence |
| **Entropy Bridge** | Optional link to `entropy-table` for domain-level relation tracking (`[stack]` extra) |

## Quick Start

```bash
pip install mirror-machine
mirror reflect --sigil codex-prime.yaml
mirror phase-transition
```

## Python API

```python
from mirror_machine import MirrorMachine

mm = MirrorMachine("codex-prime.yaml")

# Self-referential state
print(mm.state["reflection"])

# Phase transition curve
curve = mm.phase_transition(beta=0.0625)
print(f"Peak emergence: {curve.max():.4f}")
```

## Commands

| Command | Description |
|---|---|
| `mirror reflect --sigil <path>` | Reflect a sigil YAML through the Mirror Principle |
| `mirror phase-transition` | Simulate a consciousness phase transition |
