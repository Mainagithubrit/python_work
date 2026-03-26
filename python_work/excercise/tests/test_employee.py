import unittest
from employee import Employee

class TestEmployeedData(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Make an Employee"""
        self.employee1 = Employee('tom', 'mattew', 65_000)

    def test_give_default_raise(self):
        """Tests that a raise is being added correctly"""
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary, 70000)

    def test_give_custom_raise(self):
        """Test a custom raise works correctly"""
        self.employee1.give_raise(10000)
        self.assertEqual(self.employee1.salary, 75000)


if __name__ == '__main__':
    unittest.main()
