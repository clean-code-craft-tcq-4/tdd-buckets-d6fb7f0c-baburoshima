import unittest
import Current_RangeDetection

class TypewiseTest(unittest.TestCase):
  def test_getcurrentvalues(self):
    self.assertTrue(Current_RangeDetection.getcurrentvalues([4,5]) == 2)

if __name__ == '__main__':  
  unittest.main() # pragma: no cover