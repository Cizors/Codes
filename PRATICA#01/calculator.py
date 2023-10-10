def calculator(number1, number2, operation = str):
    if operation.lower() == "add":
        return print(f"Result of the Add: {number1 + number2}")
    elif operation.lower() == "subtract":
        return print(f"Result of the Subtract: {number1 - number2}")
    elif operation.lower() == "multiply":
        return print(f"Result of the Multiply: {number1 * number2}")
    elif operation.lower() == "divide":
        return print(f"Result of the Divide: {number1 // number2}")
    else:
        print(f"Invalid Operation.")
