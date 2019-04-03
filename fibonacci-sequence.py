thislist = [0,1,1]

a = 0
while(a < 10000):
    thislist[a+2] = thislist[a+1] + thislist[a]

    thislist.append(0)
    a = a + 1

print(thislist)