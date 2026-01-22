from admin import  Users, Privileges
from users import Users

first_user = Users("Francis", "Maina", 30, 'frank@gmail.com')

second_user = Users("Lisa", "Wanjiru", 25, 'lisa@yahoo.com')
third_user = Users("Terry", "Wekesa", 22, "wekesa@gmail.com")

first_user.describe_user()
first_user.greet_user()
first_user.increment_login_attempts()
print(f"Login attempts: {first_user.login_attempts}")

admin1 = Privileges()
admin1.show_privileges()

"""second_user.describe_user()
second_user.greet_user()

third_user.describe_user()
third_user.greet_user()"""
print("Reseting login attempts...")
first_user.reset_login_attempts()
print(f"Login attempts: {first_user.login_attempts}")
