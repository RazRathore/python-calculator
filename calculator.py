def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract second number from first."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide first number by second."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation():
    """Get a valid operation from user input."""
    operations = {'1': 'Addition', '2': 'Subtraction', '3': 'Multiplication', '4': 'Division', '5': 'Exit'}
    while True:
        print("\nSelect operation:")
        for key, value in operations.items():
            print(f"{key}. {value}")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in operations:
            return choice
        else:
            print("Invalid choice. Please select a valid operation.")

def main():
    """Main function to run the calculator."""
    while True:
        choice = get_operation()

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'
            
            print(f"{num1} {operation} {num2} = {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()

