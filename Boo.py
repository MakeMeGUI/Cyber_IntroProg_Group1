

def Calulate(num1, num2):
    return num1 + num2

def Print5(count):
    for i in range(0, int(count)):
        print("Hello Wrold!\n")
        print(Calulate(i, 2))

Print5(input("Number: "))