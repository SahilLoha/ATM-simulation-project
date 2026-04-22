import utils


def withdraw():
    
    amount_to_withdraw=int(input("Enter amount to withdraw: "))
    if amount_to_withdraw<=utils.balance:
        print(f"{amount_to_withdraw} is withdrawl successfully")
        print("collect your cash")
        utils.balance-=amount_to_withdraw
        print("Balnce after withdrawn",utils.balance)
        utils.transactions.append(f"Withdrawn:-{amount_to_withdraw}")
    else:
        print("insufficient balance! enter valid amount to withdraw")
    
