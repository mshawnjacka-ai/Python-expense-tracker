expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nYour Expenses:")
    for expense in expenses:
        print(
            f"{expense['name']} - "
            f"{expense['amount']:.2f} - "
            f"{expense['category']}"
        )


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()