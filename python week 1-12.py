
# SMART BANKING SYSTEM


import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Base Class (Week 7)

class Record:
    def __init__(self, rid):
        self.rid = rid

# Transaction Class (Week 6 + 7)

class Transaction(Record):
    def __init__(self, rid, date, amount, t_type, merchant, notes=""):
        super().__init__(rid)
        self.date = date
        self.amount = amount
        self.t_type = t_type
        self.merchant = merchant
        self.notes = notes
        self.tags = set()

    def add_tag(self, tag):
        self.tags.add(tag)

    def update_amount(self, amt):
        self.amount = amt

    def to_dict(self):
        return {
            "id": self.rid,
            "date": self.date,
            "amount": self.amount,
            "type": self.t_type,
            "merchant": self.merchant,
            "notes": self.notes
        }

    def display(self):
        print(f"{self.rid} | {self.date} | ₹{self.amount} | {self.t_type} | {self.merchant} | {self.notes}")


# Global Data
transactions = []
tid = 1000
FILE = "bank_data.json"



# Validation (Week 9)

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")



# Add Transaction (Week 1–5)

def add_transaction():
    global tid
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        validate_amount(amount)

        t_type = input("Enter type (credit/debit): ")
        merchant = input("Enter merchant: ")
        notes = input("Enter notes: ")

        tid += 1
        t = Transaction(tid, date, amount, t_type, merchant, notes)

        tag = input("Add tag (optional): ")
        if tag:
            t.add_tag(tag)

        transactions.append(t)
        print(" Transaction Added")

    except Exception as e:
        print(" Error:", e)



# View Transactions (Week 2)

def view_transactions():
    if not transactions:
        print("No transactions available")
        return

    for t in transactions:
        t.display()



# Search (Week 3 + 4)

def search_transaction():
    key = input("Search merchant: ").lower()

    found = False
    for t in transactions:
        if key in t.merchant.lower():
            t.display()
            found = True

    if not found:
        print("No match found")



# Save JSON (Week 8)

def save_data():
    data = [t.to_dict() for t in transactions]
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("💾 Data Saved")


# Load JSON (Week 8)

def load_data():
    global tid
    try:
        with open(FILE, "r") as f:
            data = json.load(f)

            for d in data:
                t = Transaction(
                    d["id"], d["date"], d["amount"],
                    d["type"], d["merchant"], d["notes"]
                )
                transactions.append(t)

            if transactions:
                tid = max(t.rid for t in transactions)

        print("📂 Data Loaded")

    except FileNotFoundError:
        print("No previous data found")



# NumPy Analytics (Week 10)

def numpy_analysis():
    if not transactions:
        print("No data")
        return

    amounts = np.array([t.amount for t in transactions])

    print("\n📊 NumPy Analysis")
    print("Total:", np.sum(amounts))
    print("Average:", np.mean(amounts))
    print("Max:", np.max(amounts))
    print("Min:", np.min(amounts))



# Pandas Analysis (Week 11)

def pandas_analysis():
    if not transactions:
        print("No data")
        return

    data = {
        "amount": [t.amount for t in transactions],
        "type": [t.t_type for t in transactions]
    }

    df = pd.DataFrame(data)

    print("\n📊 Pandas Summary:")
    print(df.groupby("type").sum())



# Visualization (Week 12)

def show_chart():
    if not transactions:
        print("No data")
        return

    amounts = [t.amount for t in transactions]
    labels = [t.date for t in transactions]

    plt.bar(labels, amounts)
    plt.title("Spending Chart")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.show()



# MENU SYSTEM (Week 2)

def menu():
    load_data()

    while True:
        print("\n====== SMART BANKING SYSTEM ======")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Search Transaction")
        print("4. NumPy Analysis")
        print("5. Pandas Analysis")
        print("6. Show Chart")
        print("7. Save Data")
        print("8. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_transaction()
            elif choice == 2:
                view_transactions()
            elif choice == 3:
                search_transaction()
            elif choice == 4:
                numpy_analysis()
            elif choice == 5:
                pandas_analysis()
            elif choice == 6:
                show_chart()
            elif choice == 7:
                save_data()
            elif choice == 8:
                save_data()
                print("👋 Exiting...")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Enter valid number!")

menu()