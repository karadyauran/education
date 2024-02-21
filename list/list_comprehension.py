fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# use this

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]  # for each elem in `fruits` where this x consists 'a'
print(newlist)

newlist = [x for x in fruits]  # no conditions, useless line

newlist = [x for x in range(10)]
print(newlist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x.upper() for x in fruits]  # upper all element in list `fruits`
print(newlist)

newlist = ['hello' for x in fruits]  # replaces all elements in list `fruits` to 'hello'
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]  # replaces only banana
print(newlist)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']
