thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  # ['apple', 'banana', 'watermelon', 'cherry']

# extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")  # difference
thislist.extend(thistuple)
print(thislist)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']


