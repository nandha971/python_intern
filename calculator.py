def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    
    if num2 == 0:
        return "❌ Error: Division by zero is not allowed."
    else:
        return num1 / num2



print("🧮 Welcome to the Simple Calculator!")

while True:

    print("\n" + "=" * 25)
    print("    CALCULATOR MENU     ")
    print("=" * 25)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 25)

    choice = input("Choose an option (1-5): ")

    
    if choice == "5":
        print("\nThank you for using the calculator. Goodbye! 👋")
        break  

    
    if choice in ["1", "2", "3", "4"]:
        try:
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
            continue  

        
        if choice == "1":
            result = add(n1, n2)
            print(f"📊 Result: {n1} + {n2} = {result}")

        elif choice == "2":
            result = subtract(n1, n2)
            print(f"📊 Result: {n1} - {n2} = {result}")

        elif choice == "3":
            result = multiply(n1, n2)
            print(f"📊 Result: {n1} × {n2} = {result}")

        elif choice == "4":
            result = divide(n1, n2)
            
            if isinstance(result, str):
                print(result)
            else:
                print(f"📊 Result: {n1} ÷ {n2} = {result}")

    else:
        print("❌ Invalid choice. Please select an option between 1 and 5.")