def validate_numbers(*args):
    """Validate that all provided arguments are numerical (int or float)."""
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Invalid input '{num}': All operands must be integers or floats.")

def add(a, b):
    """Return the sum of a and b with input type validation."""
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    """Return the difference of a and b with input type validation."""
    validate_numbers(a, b)
    return a - b

def multiply(a, b):
    """Return the product of a and b with input type validation."""
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b with error handling for zero division and invalid types."""
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is undefined.")
    return a / b
