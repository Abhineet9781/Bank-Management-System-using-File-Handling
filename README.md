Bank Management System Overview
This Python program implements a simple bank management system that allows users to register new accounts, access existing accounts, and perform basic banking operations such as depositing money, withdrawing money, and checking account balances.

Functionality Overview:
1. New Customer Registration (new_customer Function):
Prompts the user to enter personal information including name, father's name, address, mobile number, type of government ID, account type (saving or current), and initial deposit amount.
Validates the input data:
Ensures all fields are filled out and not left empty.
Verifies that the mobile number consists only of digits and is exactly 10 digits long.
Verifies that the deposit amount consists only of digits.
If all data is valid, registers the new account by:
Generating a unique account number (increments based on existing entries in bank_data.txt).
Appends the account details to a text file (bank_data.txt).
Displays the newly registered account details.
2. Existing Customer Access (existing_customer and other Functions):
Allows existing customers to access their accounts by entering their account number.
Retrieves account details from the bank_data.txt file based on the entered account number.
Provides options to:
Deposit money into the account.
Withdraw money from the account (if sufficient balance is available).
Check the account balance.
Key Components:
File Handling (bank_data.txt):

Stores account details in a text file (bank_data.txt).
Each account's information is stored with a unique identifier ("ACCOUNT NO.:") to distinguish between different accounts.
User Input Validation:

Ensures that user-provided data is valid (e.g., mobile number format, deposit amount format) before processing.
Menu-Driven Interface:

Presents a menu to the user with options to register as a new customer, access an existing account, or exit the program.
Based on user selection, invokes appropriate functions to perform the desired actions.
Project Description:
This bank management system provides a basic yet functional interface for managing customer accounts. It enables new customers to easily register and existing customers to perform common banking operations. The program demonstrates fundamental concepts of file handling, data validation, and menu-driven user interfaces in Python.

Note:

This system is intended for educational purposes and showcases a simplistic implementation of a bank management system. For production-level use, additional features such as enhanced security measures, database integration, and error handling would be essential. Additionally, it's important to note that storing sensitive information (like account details) in plain text files is not secure for real-world applications.
