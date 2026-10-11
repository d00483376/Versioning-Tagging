import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate(operation, a, b):
    logger.info("Calculation requested: %s, %s, %s", operation, a, b)

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            logger.warning("Division by zero attempted")
            return "Error: Cannot divide by zero"
        return a / b
    else:
        logger.warning("Unsupported operation: %s", operation)
        return "Error: Unsupported operation"

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3))        # Output: 8
    print(calculate('subtract', 5, 3))   # Output: 2
    print(calculate('multiply', 5, 3))   # Output: 15
    print(calculate('divide', 5, 3))     # Output: 1.666...
    print(calculate('divide', 5, 0))     # Error
