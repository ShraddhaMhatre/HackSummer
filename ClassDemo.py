class Car:
  total_cars = 0

  @classmethod
  def get_total_cars(cls):
    return cls.total_cars

  def __init__(self,year,make,model):
    self.year = year
    self.make = make
    self.model = model
    Car.total_cars += 1

  def __str__(self):
    return "{}{}{}".format(self.year,self.make, self.model)
