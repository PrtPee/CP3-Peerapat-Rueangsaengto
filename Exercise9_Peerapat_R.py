usernameInput = input("username : ")
passwordInput = input("password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("Please try agin")
    usernameInput = input("username : ")
    passwordInput = input("password : ")
print("Login successful")