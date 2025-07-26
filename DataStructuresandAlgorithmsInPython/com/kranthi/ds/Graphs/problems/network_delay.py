"""
A **network of *n* nodes** labeled from `1` to `n` is provided, along with a list of travel times for **directed edges**. Each edge is represented as:
```
times[i] = (xi, yi, ti)
```
Where:

* `xi` is the **source node**,
* `yi` is the **target node**,
* `ti` is the **time delay** from node `xi` to node `yi`.

Given a **starting node `k`**, the goal is to determine the **minimum time** it takes for all the remaining `n - 1` nodes to receive the signal from node `k`.
If it's not possible for all nodes to receive the signal, return `-1`.

### Constraints:

* `1 ≤ k ≤ n ≤ 100`
* `1 ≤ times.length ≤ 6000`
* `times[i].length == 3`
* `1 ≤ xi, yi ≤ n`
* `xi ≠ yi`
* `0 ≤ ti ≤ 100`
* All pairs `(xi, yi)` are **unique** — no duplicate edges.

"""

