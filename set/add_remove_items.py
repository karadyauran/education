thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)  # add another set
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)  # {'kiwi', 'orange', 'banana', 'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # {'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # {'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)  # apple
print(thisset)  # {'cherry', 'banana'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  # exception because set is undefined
