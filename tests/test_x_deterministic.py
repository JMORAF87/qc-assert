from qiskit import QuantumCircuit
from qc_assert import run_counts, assert_deterministic

def test_x_makes_one():
    qc = QuantumCircuit(1)
    qc.x(0)
    qc.measure_all()

    counts = run_counts(qc, shots=500)
    assert_deterministic(counts, "1", tol=0.001)
