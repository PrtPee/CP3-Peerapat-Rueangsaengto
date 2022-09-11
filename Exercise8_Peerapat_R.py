username = input("username : ")
password = input("password : ")
if username == "customer" and password == "123456":
    print("----------------------")
    print("Welcome to coffee shop")
    print("----------------------")
    print("Please selet your order")
    print("----------------------")

    Espresso = 40
    Americano = 40
    Latte = 50
    Cappuccino = 50
    Mocca = 55
    Macchiato = 55
    print("1.Espresso  ",Espresso,"THB")
    print("2.Americano ",Americano,"THB")
    print("3.Latte     ",Latte,"THB")
    print("4.Cappuccino",Cappuccino,"THB")
    print("5.Mocca     ",Mocca,"THB")
    print("6.Macchiato ",Macchiato,"THB")
    print("----------------------------")
    coffeeInput = int(input("Please select your coffee number : "))

    if coffeeInput == 1:
            amount = int(input("Espersso : "))
            print("price",Espresso*amount,"THB")
    elif coffeeInput == 2:
            amount = int(input("Americano : "))
            print("price",Americano*amount,"THB")
    elif coffeeInput == 3:
            amount = int(input("Latte : "))
            print("price",Latte*amount,"THB")
    elif coffeeInput == 4:
            amount = int(input("Cappuccino : "))
            print("price",Cappuccino*amount,"THB")
    elif coffeeInput == 5:
            amount = int(input("Mocca : "))
            print("price",Mocca*amount,"THB")
    elif coffeeInput == 6:
            amount = int(input("Macchiato : "))
            print("price",Macchiato*amount,"THB")
    else:
            print("Sorry!!, Please select again")
    print("---------Thank you----------")
else:
    print("Login Failed!!, Please try again")




