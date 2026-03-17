from coffy_update import takeout_order


def show_item(item):
    print(f"Item: {item['name']}, Price: ${item['price']:.2f}")


def show_total(order_list):
    total_items = len(order_list)
    total_price = sum(item['price'] for item in order_list)
    total_tax = total_price * 0.07  

    print(f"\nTotal Items: {total_items}")
    print(f"Total Price: ${total_price:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")
    print(f"Total Amount: ${total_price + total_tax:.2f}")


def dine_in_order():
    print("\n--- Dine-in Coffee Menu ---")

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

        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice in menu:
            order_list.append(menu[choice])
            print(f"You ordered {menu[choice]['name']}")
        else:
            print("Invalid choice. Try again.")
            continue

        another = input("Do you want another item? (yes/no): ")
        if another.lower() != "yes":
            break

    return order_list


def main():
    print("Welcome to the Coffee ECB Express!")

    print("\nChoose your order type:")
    print("1. Dine-in Coffee")
    print("2. Takeout Coffee")

    section = input("Enter choice (1/2): ")

    if section == "1":
        order_list = dine_in_order()
    elif section == "2":
        order_list = takeout_order()
    else:
        print("Invalid option. Exiting...")
        return

    print("\n--- Your Order Summary ---")
    for item in order_list:
        show_item(item)

    show_total(order_list)
    print("\nThank you for your order!")


if __name__ == "__main__":
    main()