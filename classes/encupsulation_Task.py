#Task #1
class Car:
    def __init__(self, speed = 0):
      if speed < 0 or speed > 200:
        raise Exception("invalid speed")
      self._speed = speed

    #gettter method 
    def get_speed(self):
      return self._speed

    def accelerate(self, speedup):
        if speedup < 0:
            raise Exception("Invalid acceleration")
          
        if (self._speed + speedup) > 200:
            raise Exception("Overspeeding after acceleration")
      
        self._speed = self._speed + speedup
         

    def brake(self, speeddown):
      if speeddown > 0:
        raise Exception("Invalid Brake")

      if (self._speed + speeddown) < 0:
        raise Exception("invalid brake")

      self._speed = self._speed + speeddown

try:
  obj = Car(10)
  print("the speed of the car is " , obj.get_speed())
  obj.accelerate(90)
  print("the speed of the car is " , obj.get_speed())
  obj.brake(-8)
  print("the current speed of the car is " , obj.get_speed())
except Exception as e:
  print(e)
  exit(1)

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
    if balance < 0:
      raise Exception("Can't start account with negative balance.")
    self._balance = balance

  def get_balance(self):
    return self._balance
     
  def deposit(self, amount):
      if amount < 0:
          raise Exception("You can't deposit negative or zero amount.")
      self._balance = self._balance + amount
      return self.get_balance()

  def withdraw(self, amount):
      if amount > self._balance:
          raise Exception("Insuficient balance.") 
      self._balance = self._balance - amount
      return self.get_balance()


account = BankAccount(-100)
 
try:
  account.deposit(50)
  print('My balance is', account.get_balance()) 
  account.withdraw(55)
  print('My balance is', account.get_balance())
except Exception as e:
  print(e)
  exit(1)
        

    
