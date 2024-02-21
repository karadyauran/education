thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry', 'banana', 'kiwi'] deletes only the first item

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # by index
print(thislist)  # ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # last item
print(thislist)  # ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]  # deletes first element
print(thislist)  # ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist  # deletes list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # cleans the list
print(thislist)  # []


