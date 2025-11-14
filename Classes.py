class Persons:

#
#Practice creating classes and methods
#
    population = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
    
    def info(self) -> str:
        return f"My name is {self.name} and I am {self.age} years old"


person1 = Persons("Mary",56)
person2 = Persons("Manny",13)
person3 = Persons("Willy",20)

print(person1.info())
print("Changing Mary to Jonathan")
person1.age = 23
person1.name = "Jonathan"
print(f"Deleting {person2.name}")
del person2

print(person1.info())