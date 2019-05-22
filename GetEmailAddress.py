# Write a function called 'GetEmailAddress' that will keep asking the user until they enter a email address with a valid format.
# A Valid format of an email address is considered as: contains an '@', at least 1 '.' and the domain name and account name is longer than 2 characters but not longer than 16.
# The function then returns the Email Address.

def GetEmailAddress():
    FormatValard = False
    Email = ""

    while(FormatValard == False):
        Email = input("Enter a valard email address: ")
        if(Email.count("@") == 1):
            if(Email.count(".") == 1):
                if(Email.index("@") > 2 and Email.index("@") <= 16):
                    if((Email.index("@") + 2) > Email.index("@") and (Email.index("@") + 16) <= Email.index("@")):
                        FormatValard = True
                        return Email
                    else:
                        print("Email can only contain more then 2 or less then 16 charactures after @ symbol")
                else:
                    print("Email can only contain more then 2 or less then 16 charactures before @ symbol")
            else:
                print("Email can only contain one . symbol")
        else:
            print("Email can only contain one @ symbol")
        print("Invalard format")

GetEmailAddress()