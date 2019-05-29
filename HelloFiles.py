myFile = open("helloworld.txt", "w")
myFile.write("Hello World")
myFile.close()

myFile = open("helloworld.txt", "r")
myFile.readable()
contence = myFile.readlines()
for line in contence:
    print(line.strip())

myFile.close()