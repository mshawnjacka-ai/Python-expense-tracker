import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["name", "amount", "category"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    name = input("Enter expense name: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": str(amount),
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n--- Your Expenses ---")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']} - "
            f"{float(expense['amount']):.2f} - "
            f"{expense['category']}"
        )


def show_total(expenses):
    total = sum(float(expense["amount"]) for expense in expenses)

    print(f"\nTotal spending: {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()