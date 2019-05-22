# Write a function called 'GetElementAt' that takes a list and index as a parameter and returns the element at the index, or None if the index is out of bounds.
# You can not use an if statement in your function (use a try except instead).
# eg: GetElementAt([1,2,3,4,5,6,7], 4) -> 5
# eg: GetElementAt([1, 2, 3], 3) -> None
# Paste only the function below.

def GetElementAt(list, index):
    try:
        return list[index]
    except IndexError:
        return None

print(GetElementAt([1,2,3,4,5,6,7], 4) == 5)
print(GetElementAt([1, 2, 3], 3) == None)