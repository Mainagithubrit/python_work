import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('Francis', 'Maina', 10000)
        self.emp_2 = Employee('Carolie', 'Wanjiru', 20000)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Francis.Maina@email.com')
        self.assertEqual(self.emp_2.email, 'Carolie.Wanjiru@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Maina@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Wanjiru@email.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Francis Maina')
        self.assertEqual(self.emp_2.fullname, 'Carolie Wanjiru')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Maina')
        self.assertEqual(self.emp_2.fullname, 'Jane Wanjiru')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 10500)
        self.assertEqual(self.emp_2.pay, 21000)


if __name__ == '__main__':
    unittest.main()
