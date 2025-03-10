"""
A simple calculator script that performs basic arithmetic operations
(addition, subtraction, multiplication, division) based on user input.
"""

import sys

def main():
    """
    Main function to execute the calculator operations.
    It either takes command-line arguments or prompts the user for input
    to perform the desired arithmetic operation.
    """
    if len(sys.argv) == 4:
        num1, num2, calc = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        calc = input("Enter the number of your choice: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input: Please enter numeric values.")
        return

    if calc == '1':
        result = num1 + num2
        operation = "sum"
    elif calc == '2':
        result = num1 - num2
        operation = "difference"
    elif calc == '3':
        result = num1 * num2
        operation = "product"
    elif calc == '4':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = num1 / num2
        operation = "quotient"
    else:
        print("Invalid input: Please select a valid operation.")
        return

    print(f"The {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
