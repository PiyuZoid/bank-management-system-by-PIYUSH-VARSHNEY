import json
import os

DATA_FILE = "bank_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(all_account_details, file, indent=4)

all_account_details = load_data()

def create_acc():
    print("Creating account...")
    name = input("Enter your full name: ")
    mobile_no = input("Enter your Mobile Number: ")
    account_number = mobile_no

    if account_number in all_account_details:
        print("Account already exists with this number!")
        return

    all_account_details[account_number] = {
        "name": name,
        "current_bal": 0,
        "transactions": []
    }

    save_data()
    print("Your account has been created.")
    print("Your account number is", mobile_no)

def check_bal():
    print("\n--- Check Balance ---")
    account_number = input("Enter your account number: ")

    if account_number in all_account_details:
        print("Your current balance is", all_account_details[account_number]["current_bal"])
    else:
        print("No account exists with the entered account number:", account_number)

def view_acc_details():
    print("\n--- View Account Details ---")
    account_number = input("Enter your account number: ")

    if account_number in all_account_details:
        details = all_account_details[account_number]
        print("-" * 30)
        print("Account Number :", account_number)
        print("Account Name   :", details['name'])
        print("Current Balance:", details['current_bal'])
        print("-" * 30)
    else:
        print("No account exists with the entered account number.")

def modify_acc_details():
    print("\n--- Modify Account Details ---")
    account_number = input("Enter your account number: ")

    if account_number in all_account_details:
        print("Current Name: ", all_account_details[account_number]['name'])
        new_name = input("Enter the new name for the account holder: ")

        all_account_details[account_number]['name'] = new_name
        save_data()
        print("Account details updated successfully.")
    else:
        print("No account exists with the entered account number.")

def credit():
    print("\n--- Credit Money ---")
    account_number = input("Enter your account number: ")

    if account_number in all_account_details:
        credit_amt = input("Enter the amount you want to credit: ")

        if credit_amt.isdigit():
            credit_amt = int(credit_amt)
            all_account_details[account_number]["current_bal"] += credit_amt
            all_account_details[account_number]["transactions"].append(("credit", credit_amt))

            save_data()
            print("Amount credited successfully.")
            print("New Balance:", all_account_details[account_number]["current_bal"])
        else:
            print("Invalid amount! Please enter numbers only.")
    else:
        print("No account exists with the entered account number:", account_number)

def debit():
    print("\n--- Debit Money ---")
    account_number = input("Enter your account number: ")

    if account_number in all_account_details:
        debit_amt = input("Enter the amount you want to debit: ")

        if debit_amt.isdigit():
            debit_amt = int(debit_amt)
            current_bal = all_account_details[account_number]["current_bal"]

            if current_bal >= debit_amt:
                all_account_details[account_number]["current_bal"] -= debit_amt
                all_account_details[account_number]["transactions"].append(("debit", debit_amt))

                save_data()
                print(debit_amt, "has been debited.")
                print("New Balance:", all_account_details[account_number]["current_bal"])
            else:
                print("Insufficient funds! Current balance is", current_bal)
        else:
            print("Invalid amount! Please enter numbers only.")
    else:
        print("Account not found with this account number.")

def close_acc():
    print("\n--- Close Account ---")
    account_number = input("Enter your account number to close: ")

    if account_number in all_account_details:
        del all_account_details[account_number]
        save_data()
        print("Account closed successfully.")
    else:
        print("Account not found.")

def menu():
    while True:
        print("=" * 40)
        print(" Welcome to PRIVATE BANK")
        print("=" * 40)
        print("Select the number against your choice: ")
        print("  1. Create a new Account")
        print("  2. Check balance in Account")
        print("  3. Credit money in Account")
        print("  4. Debit money in Account")
        print("  5. View Account Details")
        print("  6. Modify Account Details")
        print("  7. Close Account")
        print("  8. Exit the Menu")

        user_input = input("\nPlease enter your choice: ")

        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 1:
                create_acc()
            elif user_input == 2:
                check_bal()
            elif user_input == 3:
                credit()
            elif user_input == 4:
                debit()
            elif user_input == 5:
                view_acc_details()
            elif user_input == 6:
                modify_acc_details()
            elif user_input == 7:
                close_acc()
            elif user_input == 8:
                print("Exiting...")
                break
            else:
                print("Invalid option selected.")
        else:
            print("Invalid input! Please enter a number.")

        print("\n" + "*" * 40 + "\n")

    print("\nThank you for using our Banking System")
    print("*" * 40 + "\n")

menu()