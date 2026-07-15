def add(numbers):
    if len(numbers) != 3:
        return "Error: Addition requires exactly 3 numbers."
    try:
        return sum(numbers)
    except TypeError:
        return "Error: All items must be numbers."

def multiply(numbers):
    if len(numbers) != 3:
        return "Error: Multiplication requires exactly 3 numbers."
    try:
        result = 1
        for n in numbers:
            result *= n
        return result
    except TypeError:
        return "Error: All items must be numbers."

def subtract(numbers):
    if len(numbers) != 2:
        return "Error: Subtraction requires exactly 2 numbers."
    try:
        return numbers[0] - numbers[1]
    except TypeError:
        return "Error: All items must be numbers."

def get_number_input(prompt):
    """Safely gets a single positive or negative float from the user."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number (positive or negative) only.")

def confirm_exit():
    """Asks the user to confirm exit using specific words."""
    yes_options = ['yes', 'y', 'yeah']
    no_options = ['no', 'n', 'nope']
    
    while True:
        confirm = input("Are you sure you want to exit? (yes/y/yeah or no/n/nope): ").strip().lower()
        if confirm in yes_options:
            return True
        elif confirm in no_options:
            return False
        else:
            print("Invalid choice! Please choose among (yes/y/yeah) to exit or (no/n/nope) to continue.")

# --- MAIN PROGRAM LOOP ---
def run_calculator():
    while True:
        print("\n--- Scientific Calculator ---")
        print("1. Addition (Needs 3 numbers)")
        print("2. Multiplication (Needs 3 numbers)")
        print("3. Subtraction (Needs 2 numbers)")
        print("4. Exit")
        
        choice = input("Choose an operation (1-4): ").strip()
        
        if choice == '4':
            if confirm_exit():
                print("Exiting calculator. Goodbye!")
                break
            else:
                print("Returning to the calculator...")
                continue
            
        elif choice in ['1', '2']:
            print(f"\n--- Enter 3 numbers ---")
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            num3 = get_number_input("Enter third number: ")
            nums = [num1, num2, num3]
            
            if choice == '1':
                print(f"Result: {add(nums)}")
            else:
                print(f"Result: {multiply(nums)}")
                
        elif choice == '3':
            print(f"\n--- Enter 2 numbers ---")
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            nums = [num1, num2]
            
            print(f"Result: {subtract(nums)}")
            
        else:
            print("Invalid choice! Please choose among options 1, 2, 3, or 4.")

# To run the calculator:
if __name__ == "__main__":
    run_calculator()