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

#privite 
class Employ:
    def __init__(self,name,salary):
        #public member
        self.name =name
        #privite member
        self._salary = salary
        
emp = Employ("jesse" , 1000)
print("salary", emp._salary)