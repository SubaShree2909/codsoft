# Calculator Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("\nSimple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1/2/3/4/5): ").strip()
            if choice == "5":
                print("Exiting the calculator. Goodbye!")
                break
            
            if choice in ["1", "2", "3", "4"]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == "1":
                    print(f"The result is: {add(num1, num2)}")
                elif choice == "2":
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"The result is: {divide(num1, num2)}")
            else:
                print("Invalid choice! Please choose a valid operation.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()