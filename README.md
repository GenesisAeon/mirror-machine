# mirror-machine

**Theoretical Mirror Framework** – self-referential loops, consciousness phase transitions and Mirror Principle simulation for the GenesisAeon stack.

[![CI](https://github.com/GenesisAeon/mirror-machine/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/mirror-machine/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mirror-machine)](https://pypi.org/project/mirror-machine/)

---

## Install

```bash
pip install mirror-machine
# with full GenesisAeon stack integration
pip install mirror-machine[stack]
```

## CLI Usage

```bash
# Reflect a sigil YAML through the Mirror Principle
mirror reflect --sigil codex-prime.yaml

# Simulate a consciousness phase transition
mirror phase-transition --beta 0.0625 --steps 100
```

## Python API

```python
from mirror_machine import MirrorMachine

mm = MirrorMachine("codex-prime.yaml")

# Self-referential state with reflection key
print(mm.state["reflection"])

# Consciousness phase transition curve
curve = mm.phase_transition(beta=0.0625, steps=200)
print(f"Peak emergence: {curve.max():.4f}")
```

## What It Does

| Concept | Implementation |
|---|---|
| **Mirror Principle** | `reflect()` — loads YAML sigil, creates `state["reflection"]` self-reference |
| **Phase Transition** | `phase_transition()` — sigmoid × golden-ratio oscillation (φ = 0.618) |
| **Entropy Bridge** | `MirrorMachineBridge` — optional link to `entropy-table` (requires `[stack]`) |

## Structure

```
mirror-machine/
├── src/mirror_machine/
│   ├── core.py                 # MirrorMachine – reflect + phase_transition
│   ├── cli.py                  # Typer CLI: mirror reflect / mirror phase-transition
│   └── entropy_table_bridge.py # Optional entropy-table integration
├── domains.yaml                # Mirror-machine domain configuration
└── tests/
```

## Citation

**DOI** (after Zenodo release): `10.5281/zenodo.XXXXXXX`
**PyPI**: https://pypi.org/project/mirror-machine/

---

Part of the [GenesisAeon](https://github.com/GenesisAeon) stack — the self-reflective core.
