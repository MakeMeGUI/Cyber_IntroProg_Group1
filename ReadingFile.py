testFile = open("test.txt", "r")
outputFile = open("output.txt", "w")
print(testFile.read().strip())

for line in testFile:
	print("Line: ", line.strip())
	outputFile.write(line.split[0] + "\n")

testFile.close()
outputFile.close()