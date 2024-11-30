import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi accepts 2 lists of integers or floats in input and returns
a list of BMI values"""
    if len(weight) != len(height):
        raise ValueError("Both list are not the same size.")
    instance = isinstance
    if any(not instance(i, int) and not instance(i, float) for i in height):
        raise ValueError("All elements in 'height' must be integers or floats")
    if any(not instance(i, int) and not instance(i, float) for i in weight):
        raise ValueError("All elements in 'weight' must be integers or floats")
    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)
    return (weight_array / (height_array ** 2)).tolist()


def apply_limit(
        bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit accepts a list of integers or floats and an integer
representing a limit as parameters.
It returns a list of booleans (True if above the limit)."""
    instance = isinstance
    if any(not instance(i, int) and not instance(i, float) for i in bmi):
        raise ValueError("All elements in 'bmi' must be integers or floats.")
    if instance(limit, int) is not True:
        raise ValueError("'limit' must be an integer")
    limit_array = np.array(list(map(lambda x: x > limit, bmi)))
    return limit_array.tolist()
