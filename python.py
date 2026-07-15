def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        
        choice = input("Enter choice (1/2): ")

        if choice in ('1', '2'):
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
        else:
            print("Invalid Choice")

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

# Run the calculator
if __name__ == "__main__":
    calculator()