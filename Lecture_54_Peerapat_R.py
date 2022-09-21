def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">> "))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return print(vatCalculator(price1 + price2))

def vat():
    vat = 7/100
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    result = totalPrice * vat
    return print(result)


if login() == True :
    print("Login Success")
    showMenu()
    select = int(menuSelect())
    if select == 1:
        vat()
    else:
        priceCalculator()
else:
    print("Login fail,Please try agin.")

