import unittest
import currentRangeDetection_Nosort as currentRangeDetection

class currentRangeDetectionTest(unittest.TestCase):
  def test_samples_IsRangeOk(self):
    self.assertTrue(currentRangeDetection.IsRangeOk([0,15]) == True)
    self.assertTrue(currentRangeDetection.IsRangeOk([-1]) == False)
    self.assertTrue(currentRangeDetection.IsRangeOk([16]) == False)

  def test_convertion_CurrentSamples(self):
    self.assertTrue(currentRangeDetection.convert_Samples_list([3,5,4]) == [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    self.assertTrue(currentRangeDetection.convert_Samples_list([5,6,6,7,1]) == [0, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0])
    self.assertFalse(currentRangeDetection.convert_Samples_list([5,6,6,7,1]) == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0])

  def test_convertedsamples_and_count(self):
    self.assertTrue(currentRangeDetection.get_CurrentRangeslist([0, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]) == ([[1], [5, 6, 7]], [1, 4]))
    self.assertFalse(currentRangeDetection.get_CurrentRangeslist([0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0]) == ([[1], [5, 6, 7]], [1, 4]))

  def test_CurrentSampleCount_calculation(self):
    self.assertTrue(currentRangeDetection.get_CurrentSampleCount([[1], [1, 2, 1]]) == ( [1, 4]))
    self.assertFalse(currentRangeDetection.get_CurrentSampleCount([[1], [1, 2, 1]]) == ([1], [4]))
  
  def test_csv_output(self):
    self.assertTrue(currentRangeDetection.output_to_csv([[1],[5,6,6,7]],[1,4]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertFalse(currentRangeDetection.output_to_csv([[4,5]],[2]) == "Range, Readings"+'\n'+"4-4, 1"+'\n'+"5-5, 1")

  def test_currentvalues_to_csv_output(self):
    print("line 24",currentRangeDetection.getcurrentvalues([1,5,6,6,7]))
    self.assertTrue(currentRangeDetection.getcurrentvalues([1,5,6,6,7]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertTrue(currentRangeDetection.getcurrentvalues([-1, 101]) == None)

  def test_functionality(self):
    currentRangeDetection.getcurrentvalues([3, 3, 5, 4, 7,8, 10, 11,12])
    currentRangeDetection.getcurrentvalues([3, 3, 5, 4, 10, 11,12])
    currentRangeDetection.getcurrentvalues([4,5])
    currentRangeDetection.getcurrentvalues([3])
    currentRangeDetection.getcurrentvalues([8,8])
    currentRangeDetection.getcurrentvalues([5,6,6,7,1])

 
unittest.main()