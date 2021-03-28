class Car:
  def __init__(self, color, brand, country):
    self.color = color
    self.brand = brand
    self.country = country
  
  def run(self):
    print('Im Running')
  
  def stop(self):
    print('I am Stopped')
  
  def show_setup(self):
    print(self.color, self.brand, self.country)

car1 = Car("Black", "BMW", "Germany")
car1.run()
car1.stop()
car1.show_setup()