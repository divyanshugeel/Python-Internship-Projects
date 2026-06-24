import csv
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Amount", "Category"])


def add_expense():
    name = input("Enter Expense Name: ")
    amount = input("Enter Amount: ")
    category = input("Enter Category: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])

    print("Expense Added Successfully!\n")


def view_expenses():
    print("\n--- Expense List ---")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(f"Name: {row[0]}, Amount: ₹{row[1]}, Category: {row[2]}")


def total_expense():
    total = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expense: ₹{total}\n")


while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.\n")