"""
signal_prediction_utils.py
Utility functions for preparing λ values and coherence diagnostics
from IBM Quantum backend data.

Includes:
- IBM gate label parsing
- λ map extraction from backend props
"""

def parse_ecr_label(label):
    """
    Parses ECR gate labels like 'ecr12_13' into tuple (12, 13).
    Returns None if format is unexpected.
    """
    try:
        label_clean = label.replace("ecr", "")
        q0, q1 = label_clean.split("_")
        return (int(q0), int(q1))
    except:
        return None


def extract_lambda_map(gate_labels, gate_lambdas, coupling_map):
    """
    Filters and returns a dictionary of edge: λ from usable IBM ECR gates.
    Only includes valid structural edges with λ > 0.
    """
    lambda_map = {}
    for label, lam in zip(gate_labels, gate_lambdas):
        edge = parse_ecr_label(label)
        if edge and tuple(edge) in map(tuple, coupling_map) and lam > 0:
            lambda_map[tuple(edge)] = lam
    return lambda_map
