class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


p1 = Person(name="Alex", age=20)
print(p1)


class Student(Person):
    def __init__(self, name, age, year):
        Person.__init__(self, name, age)
        # super().__init__(name, age)
        self.graduationyear = 2019

    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.graduationyear)


x = Student("Mike", 23, 2019)
x.welcome()
