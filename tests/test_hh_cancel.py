from qiskit import QuantumCircuit
from qc_assert import run_counts, assert_only

def test_h_then_h_returns_zero():
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.h(0)
    qc.measure_all()

    counts = run_counts(qc, shots=1000)

    # Should be deterministic 0
    assert_only(counts, allowed={"0"}, max_other_prob=0.001)
