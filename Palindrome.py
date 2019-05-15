# Write a Python function that checks whether a passed string is palindrome or not called 'IsPalindrome' that returns either True or False.

# Write the function between the START and END tags
# START
def IsPalindrome(text):
    text = text.replace(" ", "")
    text = text.lower()
    if(text == text[::-1]):
        return True
    else:
        return False

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))