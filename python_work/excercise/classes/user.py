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

first_user = Users("Francis", "Maina", 30, 'frank@gmail.com')
second_user = Users("Lisa", "Wanjiru", 25, 'lisa@yahoo.com')
third_user = Users("Terry", "Wekesa", 22, "wekesa@gmail.com")

first_user.describe_user()
first_user.greet_user()
first_user.increment_login_attempts()
print(f"Login attempts: {first_user.login_attempts}")

"""second_user.describe_user()
second_user.greet_user()

third_user.describe_user()
third_user.greet_user()"""
print("Reseting login attempts...")
first_user.reset_login_attempts()
print(f"Login attempts: {first_user.login_attempts}")
