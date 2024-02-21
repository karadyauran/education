print("Hello")
print('Hello')

print('-------------------------')

a = "Hello"
print(a)

print('-------------------------')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print('-------------------------')

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print('-------------------------')

a = "Hello, World!"
print(a[1])  # 'e' because it placed on 1 index

print('-------------------------')

for x in "banana":
    print(x)  # we will see each letter on each new line

print('-------------------------')

a = "Hello, World!"
print(len(a))  # string length

print('-------------------------')

txt = "The best things in life are free!"
print("free" in txt)  # True

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

print('-------------------------')

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
