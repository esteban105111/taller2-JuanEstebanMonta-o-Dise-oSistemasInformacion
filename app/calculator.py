"""Business logic for the calculator operations."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b
