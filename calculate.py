import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def compute(operation, a, b):
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
    print(compute('add', 5, 3))        # Output: 8
    print(compute('subtract', 5, 3))   # Output: 2
    print(compute('multiply', 5, 3))   # Output: 15
    print(compute('divide', 5, 3))     # Output: 1.666...
    print(compute('divide', 5, 0))     # Error
