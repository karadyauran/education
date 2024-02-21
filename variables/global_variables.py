x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()  # Python is awesome

print('-------------------------')


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()  # Python is fantastic

print("Python is " + x)  # Python is awesome

print('-------------------------')


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)  # Python is fantastic


