from datetime import datetime

def main():
    name = "Nazmul Hossain"
    today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Developer Name: {name}")
    print(f"Today's Date: {today_date}")

if __name__ == "__main__":
    main()
