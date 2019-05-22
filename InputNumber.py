# Write a function called 'InputNumber' that will keep asking the user to enter a value until the value is a valid number.
# Paste only the function below.

def InputNumber():
    boolean = False
    while(boolean == False):
        try:
            int(input("Input a number: "))
            boolean = True
        except ValueError:
            print()

InputNumber()