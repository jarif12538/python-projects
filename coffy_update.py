def takeout_order():
    print("\n--- Takeout Section ---")
    
    menu = {
        1: {"name": "Cold Brew", "price": 4.00},
        2: {"name": "Iced Latte", "price": 4.50},
        3: {"name": "Frappuccino", "price": 5.00}
    }
    
    order_list = []
    
    while True:
        for key, item in menu.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")
        
        choice = int(input("\nSelect takeout item: "))
        
        if choice in menu:
            order_list.append(menu[choice])
            print(f"Added {menu[choice]['name']}")
        else:
            print("Invalid choice")
            continue
        
        another = input("Add more takeout? (yes/no): ")
        if another.lower() != "yes":
            break
    
    return order_list