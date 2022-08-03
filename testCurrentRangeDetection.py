import unittest
import currentRangeDetection

class currentRangeDetectionTest(unittest.TestCase):
  def test_IsRangeOk(self):
    self.assertTrue(currentRangeDetection.IsRangeOk([0,99]) == True)
    self.assertFalse(currentRangeDetection.IsRangeOk([-1,99]) == False)
    self.assertFalse(currentRangeDetection.IsRangeOk([0,100]) == False)

  def test_get_sorted_Samples(self):
    self.assertTrue(currentRangeDetection.get_sorted_Samples([3,5,4]) == [3,4,5])
    self.assertTrue(currentRangeDetection.get_sorted_Samples([5,6,6,7,1]) == [1,5,6,6,7])
    self.assertFalse(currentRangeDetection.get_sorted_Samples([5,6,6,7,1]) == [1,5,6,7])

  def test_get_CurrentRangeslist(self):
    self.assertTrue(currentRangeDetection.get_CurrentRangeslist([1,5,6,6,7]) == [[1],[5,6,6,7]])
    self.assertFalse(currentRangeDetection.get_CurrentRangeslist([1,5,6,6,7]) == [[1],[5],[6],[7]])
  
  def test_output_to_csv(self):
    self.assertTrue(currentRangeDetection.output_to_csv([[1],[5,6,6,7]]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertFalse(currentRangeDetection.output_to_csv([[4,5]]) == "Range, Readings"+'\n'+"4-4, 1"+'\n'+"5-5, 1")

  def test_getcurrentvalues(self):
    self.assertTrue(currentRangeDetection.getcurrentvalues([1,5,6,6,7]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertTrue(currentRangeDetection.getcurrentvalues([1,5,6,6.5,7]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertTrue(currentRangeDetection.getcurrentvalues([-1, 101]) == None)


if __name__ == '__main__':  
  unittest.main() # pragma: no cover
