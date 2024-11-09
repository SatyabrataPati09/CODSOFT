# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Main function to run the calculator
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)\n")

    # Input numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Choose the operation
    operation = input("\nChoose the operation (1/2/3/4): ")

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)

    print(f"\nThe result is: {result}")

# Run the calculator
calculator()