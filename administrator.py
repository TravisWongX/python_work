from my_user import User

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


