from colorama import Fore, Style, init
import math

init(autoreset=True)

OPERATIONS = {
    "1": "+",
    "2": "-",
    "3": "×",
    "4": "÷",
    "5": "^",
    "6": "√"
}

def get_number(prompt):
    while True:
        try:
            return float(input(Fore.CYAN + prompt))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")

def perform_operation(num1, num2, operation):
    try:
        if operation == "1":
            result = num1 + num2
            symbol = "+"
        elif operation == "2":
            result = num1 - num2
            symbol = "-"
        elif operation == "3":
            result = num1 * num2
            symbol = "×"
        elif operation == "4":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
            symbol = "÷"
        elif operation == "5":
            result = num1 ** num2
            symbol = "^"
        elif operation == "6":
            result = math.sqrt(num1)
            symbol = "√"
        else:
            return None, None
        return result, symbol
    except ZeroDivisionError:
        print(Fore.RED + "Error: Division by zero!")
        return None, None
    

def main():
    print(Fore.YELLOW + Style.BRIGHT + "\n=== PYTHON CALCULATOR ===")
    print(Fore.BLUE + "\nAvailable Operations:")

    for key, value in OPERATIONS.items():
        print(f"{Fore.WHITE}{key}. {Fore.GREEN}{value}")
    
    while True:
        operation = input(Fore.CYAN + "\nChoose operation (1 - 6) or q to Quit: ").strip().lower()
        if operation == "q":
            print(Fore.MAGENTA + "\nGoodbye!")
            break
        if operation not in OPERATIONS:
            print(Fore.RED + "Invalid choice! Please select 1 - 6")
            continue

        num1 = get_number("Enter first number: ")
        if operation != "6":
            num2 = get_number("Enter second number: ")
        else:
            num2 = None
        result, symbol = perform_operation(num1, num2 or 0, operation)

        if result is not None:
            if operation == "6":
                equation = f"√{num1} = {result}"
            else:
                equation = f"{num1} {symbol} {num2} = {result}"
            print(Fore.GREEN + Style.BRIGHT + f"\nResult: {equation}")

if __name__ == "__main__":
    main()