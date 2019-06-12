# find the numbers that are overlapping (TBD)

PrimeNumbers = open("primenumbers.md", "r")
HappyNumbers = open("happynumbers.md", "r")

PrimeNumberList = PrimeNumbers.readlines()
HappyNumberList = HappyNumbers.readlines()

n = 0

while(int(PrimeNumberList[n]) <= len(PrimeNumberList)):
    try:
        if(PrimeNumberList[n] == HappyNumberList.index(n)):
            print(PrimeNumberList[n])
        n = n + 1
    except ValueError:
        n = n + 1

PrimeNumbers.close()
HappyNumbers.close()