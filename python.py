def multiply(x, y):
    return x * y

def calculator():
    while True:
        print("\n--- Multiplication Calculator ---")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Perform multiplication
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")

        # Ask the user if they want to continue
        run_again = input("\nDo you want to calculate again? (yes/y/yeah or no/n/nope): ").strip().lower()
        
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