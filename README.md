![tests](https://github.com/JMORAF87/qc-assert/actions/workflows/tests.yml/badge.svg)
![python](https://img.shields.io/badge/python-3.11%2B-blue)

# qc-assert

Simple quantum circuit assertions for CI (Qiskit simulator).

## Install (dev)
pip install -e .
pip install pytest

## Run tests
pytest -q

## Example
Use assertions like:
- assert_only(counts, {"00","11"})
- assert_prob_close(counts, "00", 0.5, tol=0.1)
