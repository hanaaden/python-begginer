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
obj.set_speed(20)
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
        

    