# Write a function called 'PrintBoxByWidth' that prints out a box that looks like below, at the specified width.
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# x                                                          x
# xoooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
# x                                                          x
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# DO NOT add or edit any print statements in the code provided; you may only move them around your code.

# Write the function between the START and END tags
# START
def PrintBoxByWidth():
    x = 0
    y = 0

    while x <= 60 and y <= 4:
        
        if(x == 0 or x == 59 or y == 0 or y == 4):
            print("x", end='')
        elif(y == 1 or y == 3):
            print(" ", end='')
        elif(y == 2):
            print("o", end='')
        
        x = x + 1

        if(x == 60):
            x = 0
            y = y + 1
            print("")

PrintBoxByWidth()

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("x", end='')
print("o", end='')
print(" ", end='')
print("")