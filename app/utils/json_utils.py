from typing import Any
import numpy as np


def make_json_safe(obj: Any):
    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    if isinstance(obj, np.generic):
        return obj.item()

    return obj

# Converts NumPy values to JSON-safe Python types
