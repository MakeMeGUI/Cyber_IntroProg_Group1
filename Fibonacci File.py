myFile = open("Fibonacci.txt", "a")

a = 0
b = 1
c = 0
d = 0

while(d <= 30):
    c = a + b

    a = b
    b = c

    d = d + 1

myFile.write(str(a) + "\n")
myFile.close()