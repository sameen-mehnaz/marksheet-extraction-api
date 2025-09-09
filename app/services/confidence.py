import random

def compute_confidence(field_value):
    if field_value:
        return round(random.uniform(0.85, 1.0), 2)
    return round(random.uniform(0.0, 0.5), 2)
