class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Jon', 33)
print(person.name)
print(person.age)
person.name = 'Kenji'
print(person.name)
print(person.age)
