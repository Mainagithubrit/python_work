
from users import Users

class Admin(Users):
    """A simple class that represents an admin"""

    def __init__(self, first_name, last_name, age, email):
        """Initializing attributes of the parent class."""

        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()

class Privileges():
    """A simple class that represents privileges for an admin"""
    
    def __init__(self):
        """Initializing the privileges"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    
    def show_privileges(self):
        """This lists an administrator's privileges"""

        print(f"\nThis is an administrator's privilege {self.privileges}")





