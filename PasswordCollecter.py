# Get both the files we will be reading and writeing to.
inputfile = open("people-1.txt", "r")
outputfile = open("userpass.txt", "w")

# Working out from another one of my scripts.
# myFile.write("Hello World")
# myFile.close()
# myFile = open("helloworld.txt", "r")
# myFile.readable()
# contence = myFile.readlines()
# for line in contence:
#     print(line.strip())

# Read all lines from the file.
filedata = inputfile.readlines()

# Create a new varible that will be storing a single line from the file.
linedata = ''

# Start the while loop to go through each line.
for linedata in filedata:
    # Split the line from the file, to work with each part.
    data = linedata.split("|")

    # Take the first index untill we have the first characture, then make it lowercase. Start by creating the email.
    firstname = data[0]
    firstname = firstname[0]
    firstname = firstname.lower()

    # Get the last name and make it lowercase
    lastname = data[1]
    lastname = lastname.lower()

    # Create the email.
    email = firstname + lastname + "@Huawow.io"

    # For the password, get the first anme and make it lowercase.
    firstname = data[0]
    firstname = firstname.lower()

    # Get the first characture of the lastname and keep it uppercase.
    lastname = data[1]
    lastname = lastname[0]

    # Working out to know what date we are going by.
    # 1987 = 32
    # 1997 = 22
    # 2007 = 12
    # 2017 = 2
    # 2019 = 0

    # Get the age and calculate the year based on the current year.
    age = data[2]
    date = 2019-int(age)

    # Write the line to our file, with the password.
    outputfile.write(email + "|" + firstname + lastname + "_" + str(date) + "\n")

# Close both files when finshed, outside of the while loop.
inputfile.close()
outputfile.close()