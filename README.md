# qc-assert

Pytest-friendly unit test helpers for **Qiskit** quantum circuits — designed for **CI** (GitHub Actions) and regression testing.

![tests](https://github.com/JMORAF87/qc-assert/actions/workflows/tests.yml/badge.svg)

---

## Why this exists

Quantum code breaks in sneaky ways:
- SDK upgrades change behavior
- circuits drift from “correct” distributions
- notebook experiments don’t translate to production quality

**qc-assert** gives you small, focused assertions so you can:
- catch regressions early (before hardware runs)
- test probabilistic outputs with tolerances
- validate entanglement patterns (Bell/GHZ) reliably
- run everything in standard CI with `pytest`

---

## Install (dev)

```bash
pip install -e .
pip install pytest

---

## Quick example (Bell state test)

Run it locally:

```bash
python examples/bell_test.py
