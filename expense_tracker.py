expenses = []

print("=== Expense Tracker ===")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense Added Successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No Expenses Found!")
        else:
            print("\nExpenses:")
            for i, amount in enumerate(expenses, start=1):
                print(f"{i}. ₹{amount}")

    elif choice == "3":
        total = sum(expenses)
        print("Total Expense: ₹", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
