# Create array "history"
# Create varible "guesses"
# Create varible "r" and make it random between 1 and 25
# Create varible "i"

# BEGIN WHILE i isnot r
# Tell the user to guess a number bettween 1 and 25
# Put user answer to varible i
# IF i eaqules r
#   print "Dam you guessed my number."
#   print history array
# ELSE IF i < r
#   Input "You have guessed less then."
#   Add 1 to guessers varible
# ELSE IF i > r
#   Input "You have guessed greater then."
#   Add 1 to guessing varible
# add to new index with value "i" to "history"
# END IF
#
# IF guesses > 6
#   Print "You have run out of guesses. The number was " r "."
#   print the history
#   i = r
#   END IF
# Let the user close by pressing enter.
# END WHILE

import random
history = []
guesses = 0
r = random.randint(1, 25)
i = 0

while i != r:
    i = int(input("Guess a number between 1 and 25: "))
    if i == r:
        print("Dam you guessed my number.")
        print(history)
    elif i < r:
        print("You have guessed less then.")
        guesses = guesses + 1
    elif i > r:
        print("You have guessed greater then.")
        guesses = guesses + 1
    history.append(i)

    if(guesses > 6):
        print("You have run out of guesses. The number was " + str(r) + ".")
        print(history)
        i = r
input()