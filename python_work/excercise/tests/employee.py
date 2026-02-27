class Employee():
    """This is a simple class representing employee data"""

    def __init__(self, first_name, last_name, salary):
        """This initializes employee details"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        """adds annual raise by $5000"""
        self.salary += raise_amount


my_employee = Employee('Francis', 'Maina', 13000)
print(f"The original amount {my_employee.salary}")

my_employee.give_raise()
print(f'The employee name is {my_employee.first_name} {my_employee.last_name} and the salary plus raise {my_employee.salary}')
