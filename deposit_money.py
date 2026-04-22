import utils

def deposit():
    
    amount_to_deposit=int(input("Enter amount to deposit: "))
    if amount_to_deposit<100000:
        print("amount added to bank sucessfully")
        utils.balance+=amount_to_deposit
        print("balance after deposit ",utils.balance)
        utils.transactions.append(f"Deposited:+{amount_to_deposit}")
    else:
        print("larger amount! please deposit less than 100000 at one time")
