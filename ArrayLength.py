# get from user
w = input("Input some words: ")
# split into array and get the length of the array
p = len(w.split(" "))

# print the fist word
if(w.split(" ")[0] != ""):
    print(w.split(" ")[0])
# print the third word
if(p >= 3 and w.split(" ")[0] != ""):
    print(w.split(" ")[2])

# print anything that is not the first or last word.
if(p >= 3 and w.split(" ")[0] != ""):
    # put the first word into varible first
    first = w.split(" ")[0]
    # put the last word into varible last
    last = w.split(" ")[p-1]
    # remove the first word from varible w
    w = w.lstrip(first + " ")
    # remove the last word from varible w
    w = w.rstrip("" + last)
    # print the result of varible w
    print(w)