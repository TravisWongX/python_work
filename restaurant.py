class Restaurant():
    """A Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self,cuisine_type): # 给方法传递其他参数
        """Prints two pieces of information"""
        print("restaurant_name: " + self.restaurant_name)
        print("cuisine_type: " + cuisine_type) # 其他参数不加self

    def open_restaurant(self): # self不能省略
        """print a message"""
        print("The restaurant is open.")

dafu = Restaurant('DaFu', 'Chinese food')
dafu.describe_restaurant('SiChuan food')
dafu.open_restaurant()


    