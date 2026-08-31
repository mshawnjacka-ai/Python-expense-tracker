import json
import os
import stat

DATA_FILE = "data/expenses.json"

def secure_init():
    """Ensure data directory exists with restricted permissions."""
    if not os.path.exists("data"):
        os.makedirs("data", mode=0o700)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        os.chmod(DATA_FILE, stat.S_IRUSR | stat.S_IWUSR)

def sanitize_input(user_input):
    """Basic sanitization to prevent injection."""
    return str(user_input).replace("<", "").replace(">", "").strip()

def save_data(data):
    """Atomic write to prevent data corruption."""
    temp_file = f"{DATA_FILE}.tmp"
    with open(temp_file, "w") as f:
        json.dump(data, f, indent=4)
    os.replace(temp_file, DATA_FILE)

def add_expense(amount, category, description):
    try:
        amount = float(amount)
        if amount <= 0: raise ValueError
    except ValueError:
        print("Error: Invalid amount.")
        return

    # Sanitize strings
    category = sanitize_input(category)[:50] # Length limit
    description = sanitize_input(description)[:200]

    expenses = load_data()
    # Use a simple unique ID generator
    new_id = max([e['id'] for e in expenses], default=0) + 1
    
    expenses.append({
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category,
        "description": description
    })
    save_data(expenses)
