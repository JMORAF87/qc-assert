from qiskit import QuantumCircuit
from qc_assert import run_counts, assert_only, assert_prob_close

def test_bell_state():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()

    counts = run_counts(qc, shots=2000)

    assert_only(counts, allowed={"00", "11"}, max_other_prob=0.01)
    assert_prob_close(counts, "00", target=0.5, tol=0.1)
    assert_prob_close(counts, "11", target=0.5, tol=0.1)
