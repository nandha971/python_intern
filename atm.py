
balance = 1000.0  
current_pin = "6858"  


def check_balance():
    
    print(f"\n💵 Your current balance is: ${balance:.2f}")


def deposit_money():

    global balance
    try:
        amount = float(input("\nEnter the amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"✅ Success! Deposited ${amount:.2f}.")
            print(f"New Balance: ${balance:.2f}")
        else:
            print("❌ Invalid amount. Deposit must be greater than $0.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")


def withdraw_money():
    
    global balance
    try:
        amount = float(input("\nEnter the amount to withdraw: $"))
        if amount <= 0:
            print("❌ Invalid amount. Withdrawal must be greater than $0.")
        elif amount > balance:
            print("❌ Transaction Declined: Insufficient funds.")
        else:
            balance -= amount
            print(f"✅ Success! Withdrew ${amount:.2f}.")
            print(f"Remaining Balance: ${balance:.2f}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")


def change_pin():
    
    global current_pin
    old_pin = input("\nEnter your current PIN: ")

    if old_pin == current_pin:
        new_pin = input("Enter your new 4-digit PIN: ")
        
        if len(new_pin) == 4 and new_pin.isdigit():
            current_pin = new_pin
            print("✅ PIN changed successfully!")
        else:
            print("❌ PIN change failed. It must be exactly 4 digits.")
    else:
        print("❌ Incorrect current PIN. Access denied.")



print("🏪 Welcome to the Simple ATM Machine!")


pin_attempt = input("Please enter your PIN to log in: ")
if pin_attempt == current_pin:
    print("\n✅ Login Successful!")

    while True:
        
        print("\n" + "=" * 25)
        print("        ATM MENU        ")
        print("=" * 25)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        print("=" * 25)

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("\nThank you for using our ATM. Goodbye! 👋")
            break  
        else:
            print("❌ Invalid choice. Please select an option between 1 and 5.")
else:
    print("❌ Incorrect PIN. Access Denied. Goodbye.")