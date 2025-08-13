import math

def logarithm(a: int, b: int):
    """Calculates the logarithm of a number with a specified base.

    This function returns the logarithm of a to the given base b, rounded to two decimal places.

    Args:
        a: The number for which to calculate the logarithm.
        b: The base of the logarithm.

    Returns:
        The logarithm of a to base b, rounded to two decimal places.
    """
    return round(math.log(a, base=b), 2)
