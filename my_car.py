# from car import Car, ElectricCar # 从module中导入类
import car as c

my_bettle = c.Car('volkswagen', 'beetle', 2016)
print(my_bettle.get_descriptive_name())

my_tesla = c.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())