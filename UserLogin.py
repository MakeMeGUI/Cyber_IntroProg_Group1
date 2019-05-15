# Store the usernames.
UserName = ["Admin"]
# Store the passwords.
PassWord = ["1234"]
# For the number of attemps remaining.
attemps = 3
# Is the user logged in.
LoggedIn = False

# For the user to login.
def UserCheck(UserName, PassWord, attempts):
    username = input("Username: ")
    password = input("Password: ")

    try:
        if(UserName.index(username) >= -1 or PassWord.index(password) >= -1):
            print("Username and Password correct.")
            print("Welcome.")

        else:
            # Decrease attemps remaining if the user is wrong.
            attempts - 1
            if(attempts>0):
                print("Your username or password is wrong.")
                print("You have " + attempts + " left.")

    except(ValueError):
        print("Your username or password is wrong.")
        print("You have " + attempts + " left.")

    else:
        print("This system is now locked down.")

def CurrentUser(attemps):
    print("What do you want to do?")
    print("0 Lock down")
    print("1 Logout")

    UserAction = input("")

    if(UserAction == "0"):
        attemps = 0
    elif(UserAction == "1"):
        LoggedIn == False

print("Welcome please give your username.")
if(attemps > 0):
    UserCheck(UserName, PassWord, attemps)
    CurrentUser(attemps)
else:
    print("")