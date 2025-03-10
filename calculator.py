import sys

def main():
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

    cal_sum = float(num1) + float(num2)
    sub = float(num1) - float(num2)
    mul = float(num1) * float(num2)
    div = float(num1) / float(num2)

    if calc == '1':
        print(f"The sum of {num1} and {num2} is {cal_sum}")
    elif calc == '2':
        print(f"The difference of {num1} and {num2} is {sub}")
    elif calc == '3':
        print(f"The product of {num1} and {num2} is {mul}")
    elif calc == '4':
        print(f"The quotient of {num1} and {num2} is {div}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
