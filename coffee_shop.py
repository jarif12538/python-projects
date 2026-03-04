def show_item(item):
    print(f"Item: {item['name']}, Price: ${item['price']}")

def show_total(order_list):
    total_items = len(order_list)
    total_price = sum(item['price'] for item in order_list)
    total_tax = total_price * 0.07  
    print(f"\nTotal Items: {total_items}")
    print(f"Total Price: ${total_price:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")
    print(f"Total Amount: ${total_price + total_tax:.2f}")

def main():
    print("Welcome to the Coffee ECB Express!")
    print("You can order the following items:")
    
    menu = {
        1: {"name": "Espresso", "price": 2.50},
        2: {"name": "Latte", "price": 3.50},
        3: {"name": "Cappuccino", "price": 3.00},
        4: {"name": "Mocha", "price": 3.75}
    }
    
    order_list = []
    
    while True:
        for key, item in menu.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")
        
        choice = int(input("\nEnter the number of the item you want to order: "))
        
        if choice in menu:
            order_list.append(menu[choice])
            print(f"You ordered {menu[choice]['name']}. Price: ${menu[choice]['price']:.2f}")
        else:
            print("Invalid choice. Please try again.")
            continue
        
        another = input("Do you want to order another item? (yes/no): ")
        if another.lower() != "yes":
            break
    
    print("\n--- Your Order Summary ---")
    for item in order_list:
        show_item(item)
    show_total(order_list)
    print("Thank you for your order!")

if __name__ == "__main__":    
    main()