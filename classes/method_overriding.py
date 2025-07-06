# methid overriding is ability any OOP languages that allows a subclass or child class to provide
# specific implementation of methid tahat is already provided in super or parent class
# when methid in subclass hase same name the same parameter or signiture and same return type 
# as methid in supercalss then the methid in subclass is said override

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