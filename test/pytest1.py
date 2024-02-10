import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,10),20)
        self.assertEqual(calc.add(10,-10),0)
        self.assertEqual(calc.add(0,10),10)
        self.assertEqual(calc.add(-10,10),0)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,10),0)
        self.assertEqual(calc.subtract(10,-10),20)
        self.assertEqual(calc.subtract(0,10),-10)
        self.assertEqual(calc.subtract(-10,10),-20)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,10),100)
        self.assertEqual(calc.multiply(10,-10),-100)
        self.assertEqual(calc.multiply(0,10),0)
        self.assertEqual(calc.multiply(-10,10),-100)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,10),1)
        self.assertEqual(calc.divide(100,10),10)
        self.assertEqual(calc.divide(10,10),1)
        self.assertEqual(calc.divide(-10,10),-1)
        # self.assertRaises(ValueError,calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10,0)
    

if __name__ == "__main__":
    unittest.main()