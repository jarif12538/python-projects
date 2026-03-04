def show_iteam(item):
    print(f"Item: {item['name']}, Price: ${item['price']}")

def main():
    menu = [
        {"1 name": "Espresso", "price": 2.50},
        {"2 name": "Latte", "price": 3.50},
        {"3 name": "Cappuccino", "price": 3.00},
        {"4 name": "Mocha", "price": 3.75}
    ]
    choice = int(input("Enter the number of the item you want to order: "))
    if choice== 1:
        print("You ordered an Espresso.price is $2.50")
    elif choice == 2:
        print("You ordered a Latte.price is $3.50")
    elif choice == 3:
        print("You ordered a Cappuccino.price is $3.00")
    elif choice == 4:
        print("You ordered a Mocha.price is $3.75")
    else:
        print("Invalid choice. Please try again.")
if __name__ == "__main__":    
    main()