def GetPassword():
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    number = []
    characture = []
    
    a = ""
    a = input("Enter a password: ")
    
    if(a.len() > 7):
        i = 0
        while(a.indexof(lowercase[i]) !> 0):
            i = i + 1
            if(i >= 1):
                i = 0
                while(a.indexof(uppercase[i]) !> 0):
                    i = i + 1
                if(i >= 0):
                    i = 0
                    while(a.indexof(number[i]) !> 0):
                        i = i + 1
                    if(i >= 0):
                        i = 0
                    while(a.indexof(characture[i]) !> 0):
                        i = i + 1
                    if(i >= 0):






GetPassword()