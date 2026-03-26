# OOP - Object oriented programming 
# 4 Principles of OOP: abstract, inheritance, polymorphism and incapsulation  

# Classes and objects 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name} is {self.age} years old!"
    
person1 = Person("Ramazan", 19) 
person2 = Person("Adam", 20)

print(person1) 
print(person2)