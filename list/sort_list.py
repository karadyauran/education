thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  # sort the list alphabetically
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()  # sort the list numerically
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)  # sort the list based on how close the number is to 50
print(thislist)

# insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()  # first upper then lower
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)  # first lower then upper
print(thislist)


