def calculate(*args, **kwargs):
    """
    1.Perform calculations on given numbers based on the operations passed in keyword arguments.

    2.Args:
        *args: Positional arguments representing numbers.
        **kwargs: Keyword arguments representing operations (add, subtract, multiply, divide).

    3.Returns:
        dict: A dictionary containing results of all specified operations.

    4.ValueError: If invalid input or operations are provided.
    """
    # Check that all *args are numbers
    numbers = []
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError(f"Invalid input: {arg} is not a number.")
        numbers.append(arg)

    if not numbers:
        raise ValueError("No numbers provided.")
    if not kwargs:
        raise ValueError("No operations specified.")

    return process_operations(numbers, kwargs)


def process_operations(numbers, operations):
    """
    Args:
        numbers (list): Numbers to operate on.
        operations (dict): Operations to perform.

    Returns:
        dict: Results of the operations.
    """
    results = {}

    if operations.get("add"):
        results["add"] = sum(numbers)

    if operations.get("subtract"):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        results["subtract"] = result

    if operations.get("multiply"):
        result = 1
        for num in numbers:
            result *= num
        results["multiply"] = result

    if operations.get("divide"):
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            results["divide"] = result
        except ZeroDivisionError:
            results["divide"] = "Error: Division by zero."

    if not results:
        raise ValueError("No valid operations found. Use add, subtract, multiply, divide.")

    return results


# Example test run
if __name__ == "__main__":
    result = calculate(10, 5, 2, add=True, subtract=True, multiply=True, divide=True)
    print("Calculation Results:", result)
