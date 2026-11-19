# ATM Management System

accounts = {
    1001: {
        "name": "Anna",
        "pin": 1234,
        "balance": 5000,
        "history": []
    }
}

next_account_no = 1002


def create_account():
    global next_account_no

    name = input("Enter Name: ")
    pin = int(input("Set 4-Digit PIN: "))

    accounts[next_account_no] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "history": ["Account Created"]
    }

    print(f"\nAccount Created Successfully!")
    print(f"Your Account Number: {next_account_no}")

    next_account_no += 1


def login():
    acc_no = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"\nWelcome {accounts[acc_no]['name']}!")
        atm_menu(acc_no)
    else:
        print("Invalid Account Number or PIN")


def check_balance(acc_no):
    print(f"Current Balance: ₹{accounts[acc_no]['balance']}")


def deposit(acc_no):
    amount = float(input("Enter Amount to Deposit: "))

    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["history"].append(f"Deposited ₹{amount}")

    print("Deposit Successful")
    print(f"New Balance: ₹{accounts[acc_no]['balance']}")


def withdraw(acc_no):
    amount = float(input("Enter Amount to Withdraw: "))

    if amount <= accounts[acc_no]["balance"]:
        accounts[acc_no]["balance"] -= amount
        accounts[acc_no]["history"].append(f"Withdrawn ₹{amount}")

        print("Withdrawal Successful")
        print(f"Remaining Balance: ₹{accounts[acc_no]['balance']}")
    else:
        print("Insufficient Balance")


def transaction_history(acc_no):
    print("\n--- Transaction History ---")

    if len(accounts[acc_no]["history"]) == 0:
        print("No Transactions Found")
    else:
        for transaction in accounts[acc_no]["history"]:
            print(transaction)


def change_pin(acc_no):
    old_pin = int(input("Enter Old PIN: "))

    if old_pin == accounts[acc_no]["pin"]:
        new_pin = int(input("Enter New PIN: "))
        accounts[acc_no]["pin"] = new_pin

        print("PIN Changed Successfully")
    else:
        print("Incorrect Old PIN")


def transfer_money(acc_no):
    receiver = int(input("Enter Receiver Account Number: "))
    amount = float(input("Enter Amount: "))

    if receiver not in accounts:
        print("Receiver Account Not Found")
        return

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient Balance")
        return

    accounts[acc_no]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    accounts[acc_no]["history"].append(
        f"Transferred ₹{amount} to Account {receiver}"
    )

    accounts[receiver]["history"].append(
        f"Received ₹{amount} from Account {acc_no}"
    )

    print("Transfer Successful")


def mini_statement(acc_no):
    print("\n--- Last 5 Transactions ---")

    transactions = accounts[acc_no]["history"][-5:]

    if len(transactions) == 0:
        print("No Transactions")
    else:
        for t in transactions:
            print(t)


def atm_menu(acc_no):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Transfer Money")
        print("7. Mini Statement")
        print("8. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            check_balance(acc_no)

        elif choice == "2":
            deposit(acc_no)

        elif choice == "3":
            withdraw(acc_no)

        elif choice == "4":
            transaction_history(acc_no)

        elif choice == "5":
            change_pin(acc_no)

        elif choice == "6":
            transfer_money(acc_no)

        elif choice == "7":
            mini_statement(acc_no)

        elif choice == "8":
            print("Logged Out Successfully")
            break

        else:
            print("Invalid Choice")


while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank You For Using ATM")
        break

    else:
        print("Invalid Choice")