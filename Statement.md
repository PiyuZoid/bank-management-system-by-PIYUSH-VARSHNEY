Project Statement: Bank Management System



**1. Problem Statement**

In traditional manual banking or record-keeping systems, data management is often slow, prone to human error, and lacks immediate accessibility. Managing customer details, tracking account balances, and processing deposits or withdrawals manually can lead to discrepancies and inefficiency. 



There is a need for a lightweight, automated system that can simulate core banking operations, ensuring data is stored securely and persistently without the complexity of enterprise-level software. This project aims to solve the issue of temporary data loss by implementing file-based storage to maintain account records across different sessions.



**2. Scope of the Project**

The Bank Management System is a console-based application developed in Python. The scope of this project includes:



Platform: Command Line Interface (CLI).

Data Handling: Utilization of `JSON` file handling to ensure data persistence (data remains available after the program is closed).

Core Operations: The system covers the lifecycle of a bank account, including creation, financial transactions (credits/debits), updates to personal information, and account closure.

Validation: Implementation of logical checks for insufficient funds, unique account identification (via Mobile Number), and input type validation.

Limitations: This project is designed as a standalone local application and does not currently support networking, multi-user authentication, or inter-bank transfers.



**3. Target Users**

Bank Tellers/Administrators: The primary users who operate the system to perform tasks on behalf of customers (creating accounts, depositing cash, etc.).

Python Learners/Students: Users interested in understanding the practical implementation of CRUD (Create, Read, Update, Delete) operations and file handling in Python.

Small Scale Financial Managers: Individuals looking for a simple, text-based tool to track personal savings and mock transactions.



**4. High-Level Features**

The system is equipped with the following key functionalities:



**Account Management:**

&nbsp;   Create Account: Allows registration of new users using a unique Mobile Number and Name.

&nbsp;   Modify Details: Enables the updating of account holder names.

&nbsp;   Close Account: Provides functionality to permanently delete an account and its associated data.



**Financial Transactions:**

&nbsp;   Credit (Deposit): Adds funds to a specific account and updates the balance instantly.

&nbsp;   Debit (Withdrawal): Withdraws funds with strict validation to ensure the account has sufficient balance before processing.

&nbsp;   Transaction Logging: Internally records transaction types (credit/debit) and amounts for data integrity.



**Inquiry \& Reporting:**

&nbsp;   Check Balance: distinct feature to quickly query the available funds in an account.

&nbsp;   View Account Details: Displays comprehensive information, including Account Name, Account Number, and Current Balance.



**Data Persistence:**

&nbsp;   Automatically loads existing account data upon startup.

&nbsp;   Automatically saves data to `bank\_data.json` immediately after any transaction or update to prevent data loss.

