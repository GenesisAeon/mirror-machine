# API Reference

## `MirrorMachine`

```python
from mirror_machine import MirrorMachine
```

### Constructor

```python
MirrorMachine(sigil_path: str | None = None)
```

If `sigil_path` is provided, `reflect()` is called immediately.

---

### `reflect(sigil_path)`

```python
def reflect(self, sigil_path: str) -> dict[str, Any]
```

Load a YAML sigil and create a self-referential mirror state.

After calling `reflect`, `mm.state` will contain all top-level YAML keys **plus** a `"reflection"` key that is a shallow copy of those keys — embodying the Mirror Principle.

**Example**

```python
mm = MirrorMachine()
state = mm.reflect("codex-prime.yaml")
# state["reflection"] == {k: v for k, v in yaml_data.items()}
```

---

### `phase_transition(beta, steps)`

```python
def phase_transition(self, beta: float = 0.0625, steps: int = 100) -> np.ndarray
```

Simulate a consciousness phase transition.

Returns a 1-D NumPy array of shape `(steps,)` computed as:

```
t = linspace(0, 10, steps)
sigmoid(t) = 1 / (1 + exp(-beta * (t - 5)))
result(t)  = sigmoid(t) * (1 + 0.618 * sin(t * 2π))
```

| Parameter | Default | Description |
|---|---|---|
| `beta` | `0.0625` | Steepness of the sigmoid transition |
| `steps` | `100` | Number of time-steps in `[0, 10]` |

---

## `MirrorMachineBridge`

```python
from mirror_machine.entropy_table_bridge import MirrorMachineBridge
```

Requires `pip install mirror-machine[stack]` (provides `entropy-table`).

```python
bridge = MirrorMachineBridge()
bridge.add_reflection("coherence", 1.0)
bridge.export("domains.yaml")
```

Raises `ImportError` if `entropy-table` is not installed.
