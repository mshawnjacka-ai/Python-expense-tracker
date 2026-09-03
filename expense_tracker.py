import json
import os
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")


def initialize():
    """Create the data directory and JSON file if they don't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_data():
    """Load expenses from the JSON file."""
    initialize()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(expenses):
    """Save expenses to the JSON file."""
    initialize()

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def sanitize_input(user_input, max_length):
    """Clean and limit text input."""
    return str(user_input).strip()[:max_length]


def add_expense():
    """Add a new expense."""
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    category = sanitize_input(input("Enter category: "), 50)
    description = sanitize_input(input("Enter description: "), 200)

    expenses = load_data()

    new_id = max(
        [expense["id"] for expense in expenses],
        default=0
    ) + 1

    expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": round(amount, 2),
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_data(expenses)

    print("Expense added successfully!")


def view_expenses():
    """Display all recorded expenses."""
    expenses = load_data()

    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- EXPENSES ---")

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"${expense['amount']:.2f}"
        )


def show_total():
    """Display total spending."""
    expenses = load_data()

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal spending: ${total:.2f}")


def delete_expense():
    """Delete an expense by ID."""
    expenses = load_data()

    if not expenses:
        print("No expenses to delete.")
        return

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        print("Expense not found.")
        return

    save_data(updated_expenses)
    print("Expense deleted successfully.")


def main():
    """Run the expense tracker application."""
    initialize()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total spending")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()