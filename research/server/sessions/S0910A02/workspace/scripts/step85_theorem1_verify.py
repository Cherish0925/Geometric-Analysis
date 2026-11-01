#!/usr/bin/env python3
"""Verify the Theorem 1 (Lohkamp prerequisite) proof algebra."""
import json

# Test the rescaling argument
# Suppose Ric eigenvalues are [lambda_min, ..., lambda_max] all < 0
# Fix c < 0 
# Set alpha = |lambda_min| / |c|
# Then c*alpha = c * |lambda_min| / |c| = -|lambda_min| = lambda_min
# So c*alpha = lambda_min <= lambda_i for all i  ✓
# And Ric <= 0 since all lambda_i < 0                ✓

tests = []
for c in [-0.5, -1, -10, -100]:
    for lambda_min in [-0.1, -1, -5, -20]:
        lambda_max = lambda_min + abs(lambda_min) * 0.3  # some spread
        assert lambda_max < 0, "eigenvalues must be negative"
        
        alpha = abs(lambda_min) / abs(c)
        ca = c * alpha
        
        # Check: ca <= lambda_min
        assert ca <= lambda_min + 1e-15, f"Lower bound failed: ca={ca}, lmin={lambda_min}"
        # Check: ca = lambda_min (exact)
        assert abs(ca - lambda_min) < 1e-12, f"Not exact: ca={ca}, lmin={lambda_min}"
        # Check: lambda_max <= 0
        assert lambda_max < 0
        
        tests.append({
            "c": c, "lambda_min": lambda_min, "lambda_max": lambda_max,
            "alpha": alpha, "c_alpha": ca, 
            "lower_bound_holds": ca <= lambda_min + 1e-15,
            "upper_bound_holds": lambda_max <= 0,
        })

print(json.dumps({"all_tests_pass": True, "n_tests": len(tests)}, indent=2))
