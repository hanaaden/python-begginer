#Task #1
class car:
    def __init__(self , speed = 0):
        self._speed = speed
        
    #gettter method 
    def get_speed(self):
        if self._speed < 0 or self._speed > 200:
            return "Invalid speed"
        else:
            return self._speed
            
    #stter method
    def set_speed(self , speedcar):
        self._speed = speedcar
        
    def accelerate(self):
        if self._speed < 0 or self._speed > 200:
            return "Invalid speed"
        else:
            return "car accelarated to " , self._speed + 100
        
    def brake(self):
        if self._speed < 0 or self._speed > 200:
            return "Invalid speed"
        else:
            return  "Brake activated" ,  self._speed - self._speed
    
obj = car()
obj.set_speed(209)
print("the speed of the car is " , obj.get_speed())
print(obj.accelerate())
print(obj.brake())

import re

#task #2
class email:
    def __init__(self , email = ""):
        self._email = email
        
    def get_email(self):
        valid = re.match(r'^[a-z]+@', self._email ) 
        return self._email if valid else "invalid email"
    
    def set_email(self , emailcreation):
        self._email = emailcreation
        
createmail = email()
createmail.set_email("hana@gmail.com")
print(createmail.get_email())

#task 3
   class BankAccount:
  def __init__(self , balance = 0):
    self._balance = balance

  def get_balance(self):
    return self._balance
     
  def deposit(self, amount):
      if amount < 0:
          raise Exception("You can't deposit negative or zero amount.")
      else:
          self._balance = self._balance + amount
          return self.get_balance()

  def withdraw(self, amount):
      if amount > self._balance:
          raise Exception("Insuficient balance.") 
      else:
          self._balance = self._balance - amount
          return self.get_balance()


account = BankAccount()

try:
  account.deposit(50)
  print('My balance is', account.get_balance()) 
  account.withdraw(55)
  print('My balance is', account.get_balance())
except Exception as e:
  print(e)
  exit(1)
        
        

    
