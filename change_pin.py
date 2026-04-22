import utils
def change_pin():
    old_pin=int(input("enter old pin : "))
    if old_pin==utils.pin:
        new_pin=int(input("enter new pin: "))
        utils.pin=new_pin
        print("PIN changed successfully")
    else:
        print("Enter correct pin")