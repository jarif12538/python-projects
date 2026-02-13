def Show_balance(balance):
    pass
def Deposit(balance, amount):
    pass
def Withdraw(balance, amount):
    pass
balance=0
is_running = True
while is_running :
    print("Welcome to the Bank!")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Show_balance(balance)
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = Deposit(balance, amount)
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        balance = Withdraw(balance, amount)
    elif choice == 4:
        is_running = False
    else:
        print("Invalid choice. Please try again.")