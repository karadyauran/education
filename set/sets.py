thisset = {"apple", "banana", "cherry"}
print(thisset)  # {'banana', 'apple', 'cherry'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # {'banana', 'apple', 'cherry'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  # {True, 2, 'apple', 'cherry', 'banana'} because 1 and True is the same values

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)  # {'cherry', False, True, 'banana', 'apple'} 0 and False the same values

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
