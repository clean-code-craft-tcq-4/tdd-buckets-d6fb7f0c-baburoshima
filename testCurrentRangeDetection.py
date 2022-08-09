import unittest
import currentRangeDetection

class currentRangeDetectionTest(unittest.TestCase):
  def test_samples_IsRangeOk(self):
    self.assertTrue(currentRangeDetection.IsRangeOk([0,99]) == True)
    self.assertTrue(currentRangeDetection.IsRangeOk([-1]) == False)
    self.assertTrue(currentRangeDetection.IsRangeOk([101]) == False)

  def test_sorted_Samples(self):
    self.assertTrue(currentRangeDetection.get_sorted_Samples([3,5,4]) == [3,4,5])
    self.assertTrue(currentRangeDetection.get_sorted_Samples([5,6,6,7,1]) == [1,5,6,6,7])
    self.assertFalse(currentRangeDetection.get_sorted_Samples([5,6,6,7,1]) == [1,5,6,7])

  def test_sorted_samples_to_continuous_ranges(self):
    self.assertTrue(currentRangeDetection.get_CurrentRangeslist([1,5,6,6,7]) == [[1],[5,6,6,7]])
    self.assertFalse(currentRangeDetection.get_CurrentRangeslist([1,5,6,6,7]) == [[1],[5],[6],[7]])
  
  def test_csv_output(self):
    self.assertTrue(currentRangeDetection.output_to_csv([[1],[5,6,6,7]]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertFalse(currentRangeDetection.output_to_csv([[4,5]]) == "Range, Readings"+'\n'+"4-4, 1"+'\n'+"5-5, 1")

  def test_currentvalues_to_csv_output(self):
    self.assertTrue(currentRangeDetection.getcurrentvalues([1,5,6,6,7]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertTrue(currentRangeDetection.getcurrentvalues([1,5,6,6.5,7]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertTrue(currentRangeDetection.getcurrentvalues([-1, 101]) == None)

  def test_functionality(self):
    currentRangeDetection.getcurrentvalues([3, 3, 5, 4, 7,8, 10, 11,12])
    currentRangeDetection.getcurrentvalues([3, 3, 5, 4, 10, 11,12])
    currentRangeDetection.getcurrentvalues([4,5])
    currentRangeDetection.getcurrentvalues([3])
    currentRangeDetection.getcurrentvalues([5,6,6,7,1])

 
unittest.main() # pragma: no cover
