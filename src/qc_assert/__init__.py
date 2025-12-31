from qiskit.primitives import StatevectorSampler

def run_counts(qc, shots=1000):
    sampler = StatevectorSampler()
    result = sampler.run([qc], shots=shots).result()
    return result[0].data.meas.get_counts()

def normalize_counts(counts):
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items()}

def prob(counts, bitstring):
    total = sum(counts.values())
    return counts.get(bitstring, 0) / total

def assert_only(counts, allowed, max_other_prob=0.01):
    total = sum(counts.values())
    other = 1 - sum(counts.get(k, 0) for k in allowed) / total
    if other > max_other_prob:
        raise AssertionError(f"Too much probability outside {allowed}: {other:.3f}")

def assert_prob_close(counts, bitstring, target, tol=0.05):
    p = prob(counts, bitstring)
    if abs(p - target) > tol:
        raise AssertionError(f"P({bitstring})={p:.3f} not within {tol} of {target}")

def assert_deterministic(counts, bitstring, tol=0.001):
    # e.g. deterministic "0" or "00"
    assert_prob_close(counts, bitstring, target=1.0, tol=tol)
