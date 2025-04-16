"""
recursive_collapse_model.py
Core recursive coherence prediction model for GHZ circuits.
Derived from the Coherence Trilogy + IBM Quantum collapse prediction study.

This module contains:
- collapse threshold calculator
- lambda product + average
- recursive coherence predictor
"""

import numpy as np
from math import pi


def calculate_lambda_product(lambdas):
    """Returns the recursive product Λ(n) of all λ values."""
    product = 1.0
    for lam in lambdas:
        product *= lam
    return product


def calculate_lambda_avg(lambdas):
    """Returns the average λ̄ of all λ values."""
    return np.mean(lambdas)


def calculate_lambda_threshold(lambda_avg):
    """Returns the structural coherence collapse threshold from HRM: λ̄^{3.4π}"""
    return lambda_avg ** (3.4 * pi)


def predict_collapse(lambda_product, lambda_threshold):
    """Returns True if coherence is predicted to hold, False if collapse occurs."""
    return lambda_product >= lambda_threshold


def format_prediction_report(depth, lambda_product, lambda_avg, lambda_threshold, predicted, observed):
    """Returns a human-readable prediction report."""
    report = f"GHZ-{depth} Prediction\n"
    report += f"Λ(n): {lambda_product:.6f}\n"
    report += f"λ_avg: {lambda_avg:.6f}\n"
    report += f"HRM Collapse Threshold: {lambda_threshold:.6f}\n"
    report += f"Predicted: {'Hold' if predicted else 'Collapse'}\n"
    report += f"Observed: {'Hold' if observed else 'Collapse'}\n"
    report += f"{'✅ CORRECT' if predicted == observed else '❌ MISMATCH'}"
    return report
