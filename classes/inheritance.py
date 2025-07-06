#inheritance in python
#method overriddingin oython 
#operator overrudding in python 
#python uper
#multiple inheritance

# inheritance allows a class called child or derived class to inherit attributes and 
# methods from another class called parent or base attribute 
class Animal:
    def __init__(self , name):
        self.name = name 
        
    def speak(self):
        pass #placeholder methid to be over ridden by child classes 
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy")
print(dog.speak())

# example 2
class Parent1():
    def show(self):
        print("inside parent1")
        
class Parent2():
    def display(self):
        print("inside parent2")
        
class Child(Parent1,Parent2):
    def show(self):
        print("inside child")
        
obj =  Child()
obj.show()
obj.display()

#example 3
print("Grand child iheritance")
class Parent4():
    def display(self):
        print("inside parent")
        
class Child(Parent4):
    def show(self):
        print("inside child")

class Grandchild(Child):
    def show(self):
        print("inside GrandChild")
        
g = Grandchild()
g.show()
g.display()
    
