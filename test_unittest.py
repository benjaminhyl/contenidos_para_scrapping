import unittest
import calc
import figuras_geometricas

class Test_calc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)
    
    def test_shape(self):
        area = figuras_geometricas.Shape(3,4).get_area()
        self.assertEqual(area,12)
        

if __name__=="__main__":
    unittest.main()