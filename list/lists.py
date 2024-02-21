thislist = ["apple", "banana", "cherry"]
print(thislist)

# allows duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# len
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# can be different data tapes
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# using list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
