# A mini Project of working of a ATM Machine

bank_balance = 50000
atm_pin = 3314

print("******* Insert Your Card Please *************")
print("----------------Processing-------------------")

user_pin = int(input("Enter Your Transaction Pin: "))

if atm_pin == user_pin:
    while True:

        print('''
        1. Balance Enquiry
        2. Deposit Balance
        3. Withdraw Balance
        4. Exit
        ''')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Your Current balance is {bank_balance}")
        elif choice == 2:
            depo_amt = int(input("Deposit Amount: "))
            bank_balance += depo_amt
            print(f"The balance after {depo_amt} deposit is {bank_balance}")
        elif choice == 3:
            with_amt = int(input("Withdraw Amount: "))
            bank_balance -= with_amt
            print(f"The current balance after {with_amt} withdraw is {bank_balance}")
        elif choice == 4:
            break
        else:
            print("Enter Valid choice")

else:
    print("Invalid Pin. Try Again!")