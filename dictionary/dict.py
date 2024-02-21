# dictionary is ordered in latest python versions

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])
print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]  # Mustang
x = thisdict.get("model")

x = thisdict.keys()
print(x)  # dict_keys(['brand', 'model', 'year'])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)  # print as a tuple

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}


