class Car:
    def __init__(self, speed = 0):
      print('Creating a car')
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

class Road:
  def __init__(self, num_cars):
    self._num_cars = num_cars
    self._cars = []
    for i in range(num_cars):
      #calls the constructor of car class
      car = Car()
      self._cars.append(car)

  def accelarate_a_car(self, i, speedup):
    try:
      self._cars[i].accelerate(speedup)
    except Exception as e:
      print(e)

  def stop_a_car(self, i):
    curr_speed = self._cars[i].get_speed()
    
    try:
      self._cars[i].brake(-curr_speed)
    except Exception as e:
      print(e)

  def get_speed(self, i):
    return self._cars[i].get_speed()

road = Road(2)
road.accelarate_a_car(0, 20)
road.accelarate_a_car(1, 30)
print('Speed car 1', road.get_speed(0), 'Speed car 2', road.get_speed(1))
road.stop_a_car(1)
print('Speed car 1', road.get_speed(0), 'Speed car 2', road.get_speed(1))