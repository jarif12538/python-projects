import sys

def main():
    while True:
        user_input = input("Enter a number (1-100) or 'q' to quit: ")
        
        if user_input.lower() == 'q':
            print("\nThanks for using the Square Calculator. Goodbye!")
            sys.exit(0)
        
        try:
            num = int(user_input)
            if 1 <= num <= 100:
                print(f"\n   {num} × {num} = {num ** 2}\n")
            else:
                print("\nOops! Please enter a number between 1 and 100.\n")
        except ValueError:
            print("\nOops! That's not a valid number. Try again.\n")

if __name__ == "__main__":
    main()