class User():
    """A User Class"""

    def __init__(self, first_name, last_name, age, city):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        """Prints a summary of the user's information"""
        print("first_name: " + self.first_name.title())
        print("last_name: " + self.last_name.title())
        print("age: " + str(self.age) )
        print("city: " + self.city.title())

    def greet_user(self):
        """greeting"""
        print("What's up! " + self.first_name.title() + ' ' + self.last_name.title() + '\n')

user1 = User('Bruce', 'Lee', 35, 'HongKong')
user2 = User('Michael', 'Jackon', 35, 'USA')
user3 = User('Jose', 'mourinhio', 55, 'London')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()


