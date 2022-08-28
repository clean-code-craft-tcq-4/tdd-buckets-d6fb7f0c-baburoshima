import unittest
from AmpereRangeDetection import * 

class AmpereRangeDetectionTest(unittest.TestCase):
  
  
  
  

  
  
  
  

  
  
  

  
  
  
  

  
  
  
  

  
  
  

  def test_convertion_AmpereSamples(self):
    self.assertTrue(convert_Samples_list([5,6,6,7,1])[0] == [0, 1, 0, 0, 0, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0])
    self.assertFalse(convert_Samples_list([5,6,6,7,1])[0] == [0, 1, 0, 0, 0, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0])    
    self.assertTrue(convert_Samples_list([3,5,4])[0] == [0, 0, 0, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0])

  def test_convertion_AmpereSamplesOccurence(self):
    self.assertTrue(convert_Samples_list([5,6,6,7,1])[1] == [0, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]) 
    self.assertFalse(convert_Samples_list([5,6,6,7,1])[1] == [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])     
    self.assertTrue(convert_Samples_list([3,5,4])[1] == [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

  def test_convertedAmpereRanges(self):
    self.assertTrue(get_AmpereRanges([0, 1, 0, 0, 0, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0]) == [[1], [5, 6, 7]] )
    self.assertFalse(get_AmpereRanges([0, 1, 0, 0, 0, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0]) == [[1], [5, 6,6, 7]])

  def test_convertedAmpereRangesCount(self):
    self.assertTrue(get_AmpereRangesCount([0, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]) == [1, 4])
    self.assertFalse(get_AmpereRangesCount([0, 1, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]) == [1, 3])

  def test_AmpereSampleCount_calculation(self):
    self.assertTrue(get_AmpereRangesOcurrence([[1], [1, 2, 1]] )== [1, 4])
    self.assertFalse(get_AmpereRangesOcurrence(([1],[1, 2, 1])) == ([1], [4]))
  
  def test_csv_output(self):
    self.assertTrue(output_to_csv([[1],[5,6,6,7]],[1,4]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")
    self.assertFalse(output_to_csv([[4,5]],[2]) == "Range, Readings"+'\n'+"4-4, 1"+'\n'+"5-5, 1")

  def test_Amperevalues_to_csv_output(self):
    self.assertTrue(getAmperevalues([1,5,6,6,7]) == "Range, Readings"+'\n'+"1-1, 1"+'\n'+"5-7, 4")

  def test_functionality(self):
    getAmperevalues([3, 3, 5, 4, 7,8, 10, 11,12])
    getAmperevalues([3, 3, 5, 4, 10, 11,12])
    getAmperevalues([4,5])
    getAmperevalues([3])
    getAmperevalues([8,8])
    getAmperevalues([5,6,6,7,1])
#----------------------Test cases for extension----------------------------#
  def test_12bit_errorreading(self):
    self.assertTrue(Is_12bit_SensorInputOk(4095) == False)
    self.assertTrue(Is_12bit_SensorInputOk(4094) == True)
    self.assertTrue(Is_12bit_SensorInputOk(0) == True)

  def test_12bit_to_Ampere_Conversion(self):
    self.assertTrue(Convert_12bit_to_Ampere(1146) == 3)
    self.assertTrue(Convert_12bit_to_Ampere(4094) == 10)
    self.assertFalse(Convert_12bit_to_Ampere(1146) == 2.79)
    
  def test_12bitInputArray_to_AmpereArray_Conversion(self):
    self.assertTrue(Convert_12bitArray_to_AmpereArray([2047,2456,2456,2865,410]) == [5,6,6,7,1])
    self.assertTrue(Convert_12bitArray_to_AmpereArray([4095]) == None)
    self.assertTrue(Convert_12bitArray_to_AmpereArray([1230,2047,1628]) == [3,5,4] )

  def test_10bit_errorreading(self):
    self.assertTrue(Is_10bit_SensorInputOk(1023) == False)
    self.assertTrue(Is_10bit_SensorInputOk(1022) == True)
    self.assertTrue(Is_10bit_SensorInputOk(0) == True)

  def test_10bit_to_Ampere_Conversion(self):
    self.assertTrue(Convert_10bit_to_Ampere(511) == 0)
    self.assertTrue(Convert_10bit_to_Ampere(1022) == 15)
    self.assertFalse(Convert_10bit_to_Ampere(0) == -15)

  def test_10bitInputArray_to_AmpereArray_Conversion(self):
    self.assertTrue(Convert_10bitArray_to_AmpereArray([681,715,715,750,545]) == [5,6,6,7,1])
    self.assertTrue(Convert_10bitArray_to_AmpereArray([409,341,375]) == [3,5,4] )
    self.assertTrue(Convert_10bitArray_to_AmpereArray([1023]) == None )

unittest.main()