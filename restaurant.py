class Restaurant():
    """A Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints two pieces of information"""
        print("restaurant_name: " + self.restaurant_name)
        print("cuisine_type: " + self.cuisine_type) 

    def open_restaurant(self): # self不能省略
        """print a message"""
        print("The restaurant is open.")

dafu = Restaurant('DaFu', 'Chinese food')
daqing = Restaurant('DaQing', 'Qing food')
daliang = Restaurant('DaLiang', 'Liang food')

dafu.describe_restaurant()
daqing.describe_restaurant()
daliang.describe_restaurant()


dafu.open_restaurant()


    