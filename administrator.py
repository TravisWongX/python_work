class User():
    """A User Class"""

    def __init__(self, first_name, last_name, age, city):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information"""
        print("first_name: " + self.first_name.title())
        print("last_name: " + self.last_name.title())
        print("age: " + str(self.age) )
        print("city: " + self.city.title())

    def greet_user(self):
        """greeting"""
        print("What's up! " + self.first_name.title() + ' ' + self.last_name.title() + '\n')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, city, my_privileges):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges(my_privileges)


admin = Admin('admin', 'X', '20', 'NY',['can add post','can delete post','can ban user'])
admin.privileges.show_privileges()