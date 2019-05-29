myFile = open("input.txt", "w")

a = 0
b = 1
c = 0
d = 0
pipe = ""

while(d <= 8):
    c = a + b

    a = b
    b = c

    d = d + 1
    pipe = pipe + str(a) + "|"

myFile.write(pipe)
print("Sum of all Numbers is: " + str(a))

myFile.close()