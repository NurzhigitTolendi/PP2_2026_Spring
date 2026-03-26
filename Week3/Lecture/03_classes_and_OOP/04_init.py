# Classes and objects 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

person1 = Person("Jonh", 45)
person2 = Person("Fred", 40) 

print(person1.name, person1.age)     
print(person2.name, person2.age)  