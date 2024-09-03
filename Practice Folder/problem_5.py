balance = 1000  # Initial balance
choice = None

print("Welcome to the ATM!")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

while choice != 4:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your current balance is: ${balance}")
    elif choice == 2:
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f"${deposit_amount} has been deposited. Your new balance is: ${balance}")
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"${withdraw_amount} has been withdrawn. Your new balance is: ${balance}")
        else:
            print("Insufficient funds!")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

print("ATM session ended.")