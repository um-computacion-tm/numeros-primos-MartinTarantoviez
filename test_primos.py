import unittest

from primos import es_primos

class TestIsPrime (unittest.TestCase):
    def test_with_1(self):
        result = es_primos(1)
        self.assertEqual(result,True)
 
    def test_with_2(self):
        result = es_primos(2)
        self.assertEqual(result,True)      
        
    def test_with_3(self):
        result = es_primos(3)
        self.assertEqual(result,True)     
        
    def test_with_4(self):
        result = es_primos(10)
        self.assertEqual(result,False)  

    def test_with_5(self):
        result = es_primos(7)
        self.assertEqual(result,True) 

    def test_with_6(self):
        result = es_primos(14)
        self.assertEqual(result,False) 
    
    def test_with_18(self):
        result = es_primos(22)
        self.assertEqual(result,False)
        
    def test_with_23(self):
        result = es_primos(23)
        self.assertEqual(result,True)
        
    def test_with_387(self):
        result = es_primos(302)
        self.assertEqual(result,False)

    def test_with_88732(self):
        result = es_primos(800)
        self.assertEqual(result,False)
        
    def test_with_17771(self):
        result = es_primos(190000)
        self.assertEqual(result,False)
if __name__ == '__main__':
    unittest.main()