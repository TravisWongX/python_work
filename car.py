class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make  # 没有默认值的属性通过形参传值
        self.make = 'Jake' # 在这个位置会覆盖掉形参传来的值
        self.model = model 
        self.year = year
        self.odometer_reading = 0  # 有默认值的属性可以不通过形参传值
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
my_new_car.odometer_reading = 200  # 更改属性
my_new_car.read_odometer()