# methid overriding is ability any OOP languages that allows a subclass or child class to provide
# specific implementation of methid tahat is already provided in super or parent class
# when methid in subclass hase same name the same parameter or signiture and same return type 
# as methid in supercalss then the methid in subclass is said override

class Animal:
  def __init__(self, name):
      self.name = name 
    
  def speak(self):
      print(self.name, 'spoke')

class Dog(Animal):
   
  def speak(self):
      super().speak()
      print(self.name, 'barks')



dog = Dog('Tom')
dog.speak()

# Circle is-a shape
# Rectangle is-a shape

class Shape:
  def area(self): # Default
    return None

class Circle (Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self): # Specific
    return 3.14 * self.radius * self.radius

class Rectangle (Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self): # Specific
    return self.length * self.width

c = Circle(10)
print(c.area())

r = Rectangle(10, 20)
print(r.area())

class Parent():
    def __init__(self):
        self.value = "inside parent"
        
    def show(self):
        print(self.value)
        
class Child(Parent):
    
    def __init__(self):
        super().__init__()
        #super() function is used to call the parent class's methods
        self.value = "inside child"
        
    def show(self):
        print(self.value)
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

#why we override ?
# allows subclasesto provide specific NotImplementation of methid tha is already defined in its parent class