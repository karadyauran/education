# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry

print('-------------------------')

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange

print('-------------------------')

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry
