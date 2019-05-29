#*-------------------------------------*-------------------------------------*
#|                                     |                                     |
#|                                     |                                     |
#|                                     |                                     |
#|                                     |                                     |
#|                                     |                                     |
#|                                     |                                     |
#*-------------------------------------*-------------------------------------*

myFile = open("drawing.txt", "w")

x = 0
y = 0

while x <= 76 and y <= 7:
    
    if(x == 0 or x == 38 or x == 76):
        if(y == 0 or y == 7):
            myFile.write("*")
        else:
            myFile.write("|")
    elif(y == 0 or y == 7):
        myFile.write("-")       
    elif(y >= 1 or y <= 6):
        myFile.write(" ")

    x = x + 1

    if(x == 77):
        x = 0
        y = y + 1
        myFile.write("\n")

#write("\n")
#write("-")
#write("*")
#write(" ")
#write("|")

myFile.close()