# CLI Reference

## `mirror reflect`

Load and self-reflect a sigil YAML through the Mirror Principle.

```
Usage: mirror reflect [OPTIONS]

Options:
  --sigil TEXT  Path to sigil YAML file [default: codex-prime.yaml]
```

**Examples**

```bash
mirror reflect --sigil codex-prime.yaml
mirror reflect --sigil domains.yaml
```

---

## `mirror phase-transition`

Simulate a consciousness phase transition using sigmoid × golden-ratio oscillation.

```
Usage: mirror phase-transition [OPTIONS]

Options:
  --beta FLOAT    Transition steepness [default: 0.0625]
  --steps INTEGER Number of simulation steps [default: 100]
```

**Examples**

```bash
# Default gentle emergence
mirror phase-transition

# Steeper transition
mirror phase-transition --beta 1.0

# High-resolution simulation
mirror phase-transition --beta 0.0625 --steps 500
```

The peak value reflects the maximum emergence amplitude:
`sigmoid(t) × (1 + φ · sin(t · 2π))` where φ = 0.618 (golden ratio).
