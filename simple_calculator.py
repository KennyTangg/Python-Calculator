# ==================================================
# File Name: simple_calculator.py
# Author: Kenny Tang
# Date: 2024-09-05
# Description: A simple calculator for basic arithmetic operations.
# License: MIT License
# ==================================================

def add(x: float, y: float) -> float:
    return x + y 

def sub(x: float, y: float) -> float:
    return x - y

def mul(x: float, y: float) -> float:
    return x * y

def div(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def get_number(x: str) -> float:
    while True:
        try:
            return float(input(x))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print('''
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
    ''')

    choice = input("Choose an option (1/2/3/4): ")

    if choice in {"1", "2", "3", "4"}:
        num1 = get_number("Input Number 1: ")
        num2 = get_number("Input Number 2: ")

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {sub(num1, num2)}")
        elif choice == "3":
            print(f"Result: {mul(num1, num2)}")
        elif choice == "4":
            try:
                print(f"Result: {div(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid Choice. Please Try Again.")
        main() 

if __name__ == "__main__":
    print(" === Simple Calculator === ")
    main()