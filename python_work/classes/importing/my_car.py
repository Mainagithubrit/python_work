from car import Car
from electric_car import ElectricCar

my_car = Car('range rover', 'd110', 2016)
print(my_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadstar', 2019)
print(my_tesla.get_descriptive_name())
