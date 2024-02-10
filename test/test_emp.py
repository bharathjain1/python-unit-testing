import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("Bharath", "jain", 5000)
        self.emp_2 = Employee("Sue", "Smith", 70000)
    
    def test_email(self):

        self.emp_1.first = "Sharath"
        self.emp_2.first = "Due"

        self.assertEqual(self.emp_1.email,"Sharath.jain@gmail.com")
        self.assertEqual(self.emp_2.email,"Due.Smith@gmail.com")

    def test_fullname(self):

        self.emp_1.first = "Sharth"
        self.emp_2.first = "Corey"

        self.assertEqual(self.emp_1.fullname,"Sharth jain")
        self.assertEqual(self.emp_2.fullname,"Corey Smith")

if __name__ == "__main__":
    unittest.main()