from car import Car
from electric_car import ElectricCar as EC

my_new_car = Car("Audi", "A4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.get_odometer()

my_new_car.set_odometer(2548)
my_new_car.get_odometer()

my_new_car.set_odometer(158)
my_new_car.update_odometer(2500)
my_new_car.update_odometer(-2500)
my_new_car.get_odometer()

my_leaf = EC("Nissan", "Leaf", 2018)
print(my_leaf.get_descriptive_name())
