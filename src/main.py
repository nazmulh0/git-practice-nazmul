from datetime import datetime
from utils import add, subtract, multiply, divide

def safe_calculate(operation_name, func, *args):
    """Safely execute a math operation and catch potential errors."""
    try:
        result = func(*args)
        args_formatted = ", ".join(str(arg) for arg in args)
        print(f"[{operation_name}] ({args_formatted}) = {result}")
    except (ZeroDivisionError, TypeError) as error:
        print(f"[{operation_name}] Error: {error}")

def main():
    name = "Nazmul Hossain"
    today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Developer Name: {name}")
    print(f"Today's Date: {today_date}")
    
    print("\n--- Standard Calculator Operations ---")
    safe_calculate("Addition", add, 10, 5)
    safe_calculate("Subtraction", subtract, 10, 5)
    safe_calculate("Multiplication", multiply, 10, 5)
    safe_calculate("Division", divide, 10, 5)

    print("\n--- Error Handling Tests ---")
    safe_calculate("Division by Zero", divide, 10, 0)
    safe_calculate("Invalid Input Type", add, 10, "five")

if __name__ == "__main__":
    main()
