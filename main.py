import csv
import os


FILE_NAME = "expenses.csv"


# -----------------------------------------
# Create CSV file if it does not exist
# -----------------------------------------
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Category",
                "Description",
                "Amount"
            ])


# -----------------------------------------
# Get valid amount
# -----------------------------------------
def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Invalid amount! Please enter a number.")


# -----------------------------------------
# Add Expense
# -----------------------------------------
def add_expense():

    print("\n========== ADD EXPENSE ==========")

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    amount = get_amount()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            date,
            category,
            description,
            amount
        ])

    print("\nExpense added successfully!")


# -----------------------------------------
# View Expenses
# -----------------------------------------
def view_expenses():

    print("\n========== ALL EXPENSES ==========")

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        print(
            f"{'Date':<15}"
            f"{'Category':<15}"
            f"{'Description':<20}"
            f"{'Amount':>10}"
        )

        print("-" * 60)

        for expense in expenses:

            print(
                f"{expense['Date']:<15}"
                f"{expense['Category']:<15}"
                f"{expense['Description']:<20}"
                f"{expense['Amount']:>10}"
            )


# -----------------------------------------
# Filter Expenses
# -----------------------------------------
def filter_expenses():

    print("\n========== FILTER EXPENSES ==========")

    category = input("Enter category to filter: ").strip().lower()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        found = False

        print(
            f"\n{'Date':<15}"
            f"{'Category':<15}"
            f"{'Description':<20}"
            f"{'Amount':>10}"
        )

        print("-" * 60)

        for expense in reader:

            if expense["Category"].lower() == category:

                print(
                    f"{expense['Date']:<15}"
                    f"{expense['Category']:<15}"
                    f"{expense['Description']:<20}"
                    f"{expense['Amount']:>10}"
                )

                found = True

        if not found:
            print("No expenses found for this category.")


# -----------------------------------------
# Category Summary
# -----------------------------------------
def category_summary():

    print("\n========== CATEGORY SUMMARY ==========")

    summary = {}

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for expense in reader:

            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No expenses found.")
        return

    for category, total in summary.items():

        print(f"{category}: ₹{total:.2f}")

    grand_total = sum(summary.values())

    print("-" * 30)
    print(f"Total Expenses: ₹{grand_total:.2f}")


# -----------------------------------------
# Main Menu
# -----------------------------------------
def main():

    create_file()

    while True:

        print("\n====================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("====================================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            filter_expenses()

        elif choice == "4":

            category_summary()

        elif choice == "5":

            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:

            print("Invalid choice! Please select 1 to 5.")


# -----------------------------------------
# Start Program
# -----------------------------------------
if __name__ == "__main__":
    main()