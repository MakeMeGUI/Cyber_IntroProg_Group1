a = 0
b = 0
c = 1
while(a < 10000):
    c = a + b

    a = b
    b = c

print(a)