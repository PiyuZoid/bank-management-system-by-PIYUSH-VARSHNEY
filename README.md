# bank-management-system-by-PIYUSH-VARSHNEY
The Bank Management System is a Python-based console application that allows users to create and manage bank accounts. It supports operations like account creation, balance check, credit, debit, update details, and account closure. Data is stored persistently using JSON for secure and efficient handling.
**Bank Management System**

A simple command-line based Bank Management System built using Python.
It allows users to create and manage bank accounts with basic operations such as credit, debit, view details, modify details, check balance, and close account.
All account data is stored in a JSON file (bank_data.json), ensuring persistent storage.

**Features**

⦁	Create a new bank account
⦁	Check available account balance
⦁	Credit money to an account
⦁	Debit money from an account
⦁	View account holder details
⦁	Modify account holder name
⦁	Close/delete an account
⦁	Transaction history stored in JSON format
⦁	Validations for correct numeric input
⦁	All data is saved automatically

**Project Structure**

Bank Management System
│
├── bank_management_system.py   # Main application file
├── bank_data.json              # Auto-generated data storage file
└── README.md                   # Documentation file

**How It Works**

⦁	Each account is identified using the mobile number as the account number.
⦁	The system reads data from bank_data.json using load_data() function.
⦁	Any change in data (credit, debit, create account, etc.) is saved using save_data() function.

**How to Run**

Step 1: Install Python (if not already installed)
Download from https://www.python.org/downloads/

Step 2: Save the script as:
bank_management_system.py

Step 3: Run the program
python bank_management_system.py

**Menu Options**
Option	Description

1.	Create new account
2.	Check balance
3.	Credit money
4.	Debit money
5.	View account details
6.	Modify account holder name
7.	Close account
8.	Exit the system
