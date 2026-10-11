import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def compute(data):
    operation = data["operation"]
    a = data["a"]
    b = data["b"]

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
    elif operation == 'power':
        return a ** b
    else:
        logger.warning("Unsupported operation: %s", operation)
        return "Error: Unsupported operation"

# Example usage
if __name__ == "__main__":
    print(compute({"operation": "add", "a": 5, "b": 3}))
    print(compute({"operation": "subtract", "a": 5, "b": 3}))
    print(compute({"operation": "multiply", "a": 5, "b": 3}))
    print(compute({"operation": "divide", "a": 6, "b": 3}))
    print(compute({"operation": "divide", "a": 5, "b": 0}))
    print(compute({"operation": "power", "a": 2, "b": 3}))
