# the concept of encupsulation is bundling data and methods within single unit 
# when you create class you are emplementing a encupsalation 
# means class binds all data members(instance variable) and methods into single unit

#let we create employee class 
#the attributes such name and salary as instance varaible 
# implementing behavior using work() and show() instance methods

class Employee:
    def __init__(self , name , salary , project):
        self.name = name
        self.salary = salary
        self.project = project
    #methods 
    #to display employee details 
    def show(self):
        print("name: ", self.name , "salary" , self.salary)
        
#methods
    def work(self):
        print(self.name, "is working on " , self.project)
        
#creating object of class
emp = Employee('jesse' , 300, 'NLP')
emp.show()
emp.work()
         
# Public Member: Accessible anywhere from otside oclass.
# Private Member: Accessible within the class
# Protected Member: Accessible within the class and its sub-classes

#protected 
print("printong the protected class")
class Protected:
    def __init__(self):
        self._age = 89
class Subclass(Protected):
    def display_age(self):
        print(self._age)
obj = Subclass() 
obj.display_age() 
# Explanation
# protected attribute _age thisattribute is prefixed with single underscore the subcalss 
# inherits from protected with in this subclass we can still
# access the peotected variable 
# - methid of display_age within the subclass accesses the protected attribute 
# and print it value 
# means protected Attributes can be accessed within the class and the subclass 


#privite 
class private:
    def __init__(self):
        self.__salary = 1000
        
    def salary(self):
        return self.__salary
        
obj = private()
print(obj.salary())
# the attribute is privite the plic method provides only the way to access the private variable
# from outside is safe;y returns the value 
# trying to access the provate attribute directky obj.__salry will result AttributeError

#getters and setters 
class go:
    def __init__(self, age = 0):
        self._age = age
        
    #gettter method 
    def get_age(self):
        return self._age
    
    #stter method
    def set_age(self , x):
        self._age = x
appear = go()
#setting the age using setter
appear.set_age(22)
print(appear.get_age())
print(appear._age)