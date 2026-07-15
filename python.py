def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Choice")

        # Ask the user if they want to continue
        # .strip().lower() handles extra spaces and capital letters (like "Yes" or "NO")
        run_again = input("\nDo you want to continue? (yes/y/yeah or no/n/nope): ").strip().lower()
        
        if run_again in ('no', 'n', 'nope'):
            print("Goodbye!")
            break
        elif run_again in ('yes', 'y', 'yeah'):
            continue
        else:
            print("Unknown response, exiting by default. Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()