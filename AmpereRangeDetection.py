import itertools
from A2DConversion import *

MAX_LIMIT = 15
MIN_LIMIT = 0


def getAmperevalues(AmpereSamples):
    converted_AmpereSamples , converted_AmpereSamplesCount = convert_Samples_list(AmpereSamples)
    AmpereRanges = get_AmpereRanges(converted_AmpereSamples)
    AmpereRanges_SamplesCount = get_AmpereRangesCount(converted_AmpereSamplesCount)
    message = output_to_csv(AmpereRanges,AmpereRanges_SamplesCount)
    print(message)
    return message

def convert_Samples_list(AmpereSamples):
    sample_count = []
    Amperes_list = []
    occurence = 1
    number_list = list(range(MAX_LIMIT))
    for i in number_list:
        if i in AmpereSamples:
            occurence = AmpereSamples.count(i)
            sample_count.append(occurence)
            Amperes_list.append(i)
        else:
           sample_count.append(0)
           Amperes_list.append(0)
    return Amperes_list, sample_count

def get_AmpereRanges(converted_AmpereSamples):
    AmpereRange = []
    AmpereRange = [list(y) for x, y in itertools.groupby(converted_AmpereSamples, lambda z: z == 0) if not x]
    return AmpereRange

def get_AmpereRangesCount(converted_AmpereSamplesCount):
    AmpereRange_SampleCount = []
    AmpereRange_SampleCount = [list(y) for x, y in itertools.groupby(converted_AmpereSamplesCount, lambda z: z == 0) if not x]
    return get_AmpereRangesOcurrence(AmpereRange_SampleCount)

def get_AmpereRangesOcurrence(AmpereRanges_Samples):
    AmpereRanges_SamplesCount = []
    for item in range(0,len(AmpereRanges_Samples)):
        AmpereRanges_SamplesCount.append(sum(AmpereRanges_Samples[item]))
    return AmpereRanges_SamplesCount

def output_to_csv(AmpereRanges_list,AmpereRanges_SamplesCount):
    csv_string_list = []
    output_csv_string = ""
    csv_string_list.append(f"Range, Readings")
    for list_item,item in zip(AmpereRanges_list,range(0,len(AmpereRanges_SamplesCount))):
        csv_string_list.append(f"{list_item[0]}-{list_item[-1]}, {AmpereRanges_SamplesCount[item]}")
    output_csv_string = "\n".join(csv_string_list)
    return output_csv_string

def Convert_DigitalInput_to_AmpereArray(sensorReadingInputs, A2Dbits):
    AmpereSamples = []
    for item in sensorReadingInputs:
        if Is_SensorInputOk(item,A2Dbits):
            AmpereSamples.append(Convert_Digital_to_Ampere(item,A2Dbits))
        else:
            return None
    getAmperevalues(AmpereSamples)
    return AmpereSamples








