from datetime import datetime
from utils import add, subtract, multiply, divide

def main():
    name = "Nazmul Hossain"
    today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Developer Name: {name}")
    print(f"Today's Date: {today_date}")
    
    # Calculator operations
    num1, num2 = 10, 5
    print("\n--- Basic Calculator Operations ---")
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    main()
