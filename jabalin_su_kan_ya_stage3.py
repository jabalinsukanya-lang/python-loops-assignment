# Take input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == "+":
    result = num1 + num2
    print("Result =", result)

elif operator == "-":
    result = num1 - num2
    print("Result =", result)

elif operator == "*":
    result = num1 * num2
    print("Result =", result)

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
        print("Result =", result)

else:
    print("Invalid operator.")
    result = None

# Stage 2: Check Result (only if result exists)
if result is not None:
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")