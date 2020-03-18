class Restaurant():
    """A Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints two pieces of information"""
        print("restaurant_name: " + self.restaurant_name)
        print("cuisine_type: " + self.cuisine_type) 

    def open_restaurant(self): # self不能省略
        """print a message"""
        print("The restaurant is open.")
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['lettuce', 'carrot', 'pepperoni', 'orange']

    def display_flaovrs(self):
        for flavor in self.flavors:
            print(flavor)

icecream = IceCreamStand('aaa', 'icecream')
icecream.display_flaovrs()
icecream.open_restaurant()
print(icecream.number_served)