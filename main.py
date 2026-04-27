from display_balance import check_balance
from withdraw_money import withdraw
from deposit_money import deposit
from change_pin import change_pin 
from show_statement import show_statement
from utils import *
entered_pin=int(input("enter your pin: "))

if entered_pin ==pin:
    while True:
        print("WELCOME TO ATM")
        print("\n1. Check balance")
        print("\n2. Deposit money")
        print("\n3. Withdrawl money")
        print("\n4. Change PIN")
        print("\n5. Show Statement")
        print("\n6. Exit")

        choice=int(input("enter your choice : "))
        
        if choice==1: check_balance()
        elif choice==2: deposit()
        elif choice==3: withdraw()
        elif choice==4: change_pin()
        elif choice==5: show_statement()
        elif choice==6:
            print("Thannk You")
            break
        else:
            print("Invalid choice..!!")

else:
    print("Invalid pin..!!")

