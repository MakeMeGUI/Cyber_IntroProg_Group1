for count in range(26): print(count)

count = 0

while(count <= 40):
    print(count)
    count = count + 2

count = 0
addition = 0

n = int(input("Enter a number: "))
while(count <= n):
    addition = addition + count
    count = count + 1
    print(addition)

responce = ""

while(responce != "It gets wet"):
    responce = input("What happens when you throw a yellow rock in the red sea?")