NUMS = ["HI", "BOB", "go"]

i = 0
while(i < len(NUMS)):
    print(NUMS[i])
    i = i + 1

for y in NUMS:
    print(y)

z = ""
# Return the largest element in the list.
for y in NUMS:
    if len(y) > len(z):
        z=y

print(z)

# Join two lists.
letters = ["a","b","c"]
numbers = [1,2,3]

ln = letters + numbers
print(ln)

# Takes numbers and returns each diget.
numarray = []
numarray = input("Numbers: ")
for x in range(len(numarray)):
    print(numarray[x])

# Morse code for "a".
num = input("Anything: ")
i = 0
letarray = []

while len(num) > i:
    letarray.append(num[i])
    i = i + 1

i = 0

while i < len(letarray):
    if letarray[i] is "a":
        letarray[i] = ".-"
    i = i + 1

for a in letarray:
    print(a)