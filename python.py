def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def subtract(x, y, z):
    return x - y - z

def multiply(x, y, z):
    return x * y * z

def get_number(prompt):
    """Repeatedly asks the user for a valid positive or negative number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter numbers only (positive or negative).")

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add (2 numbers)")
        print("2. Divide (2 numbers)")
        print("3. Subtract (3 numbers)")
        print("4. Multiply (3 numbers)")
        
        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice in ('1', '2'):
            # Operations requiring 2 variables
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")

        elif choice in ('3', '4'):
            # Operations requiring 3 variables
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            num3 = get_number("Enter third number: ")

            if choice == '3':
                print(f"\nResult: {num1} - {num2} - {num3} = {subtract(num1, num2, num3)}")
            elif choice == '4':
                print(f"\nResult: {num1} * {num2} * {num3} = {multiply(num1, num2, num3)}")

        else:
            print("Invalid Choice. Please choose a number from 1 to 4.")
            continue

        # Ask the user if they want to continue
        run_again = input("\nDo you want to continue? (yes/y/yeah or no/n/nope): ").strip().lower()
        
        if run_again in ('no', 'n', 'nope'):
            print("Goodbye!")
            break
        elif run_again in ('yes', 'y', 'yeah'):
            continue
        else:
            print("Unknown response, exiting. Goodbye!")
            break

if __name__ == "__main__":
    calculator()