
class Users:
    """A simple class that represents users"""

    def  __init__(self, first_name, last_name, age, email):
        """Initializing our users first and last name"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """A method that describes our users"""

        print(f"\nMy name is {self.first_name} {self.last_name}, I am "\
            f"{self.age} years old and this is my email '{self.email}'.\n"
              )

    def greet_user(self):
        """A function that greets a user"""

        print(f"Hello,{self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """This increments login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """This method resets login attempts to 0"""
        self.login_attempts = 0
