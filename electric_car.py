class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptvie_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("You need to fill 100 gallon")
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70 # 添加子类独有属性

    def describe_battery(self): # 添加子类独有方法
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

    

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptvie_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

benz = Car('Benz', 'c60', '2019')
benz.fill_gas_tank()


