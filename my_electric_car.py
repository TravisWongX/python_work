from car import ElectricCar as E

my_tesla = E('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.get_range()