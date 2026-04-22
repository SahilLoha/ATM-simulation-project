from utils import *
def show_statement():
    print("\n---Mini Statement---\n")
    if len(transactions)==0:
        print("No Transaction yet.")
    else:
        for t in transactions:
            print(t)