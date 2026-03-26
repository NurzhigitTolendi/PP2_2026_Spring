# Classes and objects 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def greeting(self):
        print(f"Hello, {self.name}!") 

class Student(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID 
    
    def __str__(self):
        return super().__str__() + f" with ID of {self.ID}! " 
    
student1 = Student("Nurlan", 18, "25B012345") 

print(student1) 