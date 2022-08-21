MAX_LIMIT = 15
MIN_LIMIT = 0

def getcurrentvalues(CurrentSamples):
    if IsRangeOk(CurrentSamples):
        converted_CurrentSamples = convert_Samples_list(CurrentSamples)
        CurrentRanges_list,CurrentRanges_SamplesCount = get_CurrentRangeslist(converted_CurrentSamples)
        message = output_to_csv(CurrentRanges_list,CurrentRanges_SamplesCount)
        print(message)
    else:
        return None
    return message

def IsRangeOk(values):
    for item in values:
        if item in range (MIN_LIMIT, MAX_LIMIT):
            return True
    return False

def convert_Samples_list(CurrentSamples):
    sample_list = []
    occurence = 1
    number_list = list(range(MAX_LIMIT))
    for i in number_list:
        if i in CurrentSamples:
            occurence = CurrentSamples.count(i)
            sample_list.append(occurence)
        else:
           sample_list.append(0)
    return sample_list

def get_CurrentRangeslist(converted_CurrentSamples):
    CurrentRanges_Samples = []
    CurrentRanges_Values = []
    for index in range(MAX_LIMIT):
        if (converted_CurrentSamples[index] != 0 ):
            CurrentRanges_Values.append(index)
            CurrentRanges_Samples.append(converted_CurrentSamples[index])
    CurrentRanges_Values,CurrentRanges_SamplesCount = convert_currentrange(CurrentRanges_Values,CurrentRanges_Samples)
    return CurrentRanges_Values, CurrentRanges_SamplesCount

def get_CurrentSampleCount(CurrentRanges_Samples):
    CurrentRanges_SamplesCount = []
    for item in range(0,len(CurrentRanges_Samples)):
        CurrentRanges_SamplesCount.append(sum(CurrentRanges_Samples[item]))
    return CurrentRanges_SamplesCount
    
def convert_currentrange(CurrentRanges_Values,CurrentRanges_Samples):
    interval = 1
    CurrentRanges_list = []
    CurrentRanges_PrepList =[]
    CurrentRanges_SamplesCount = []
    CurrentRanges_PrepSamplesCount =[]
    for index in range(0,len(CurrentRanges_Values)):
        if (CurrentRanges_Values[index ] - CurrentRanges_Values[index-interval] > interval):
            CurrentRanges_list.append(CurrentRanges_PrepList )
            CurrentRanges_PrepList = []
            CurrentRanges_PrepList.append(CurrentRanges_Values[index])
            CurrentRanges_SamplesCount.append(CurrentRanges_PrepSamplesCount )
            CurrentRanges_PrepSamplesCount = []
            CurrentRanges_PrepSamplesCount.append(CurrentRanges_Samples[index])
            continue
        else:
            CurrentRanges_PrepList.append(CurrentRanges_Values[index])
            CurrentRanges_PrepSamplesCount.append(CurrentRanges_Samples[index])
    CurrentRanges_list.append(CurrentRanges_PrepList) 
    CurrentRanges_SamplesCount.append(CurrentRanges_PrepSamplesCount)
    return CurrentRanges_list , get_CurrentSampleCount( CurrentRanges_SamplesCount)

def output_to_csv(CurrentRanges_list,CurrentRanges_SamplesCount):
    csv_string_list = []
    output_csv_string = ""
    csv_string_list.append(f"Range, Readings")
    for list_item,item in zip(CurrentRanges_list,range(0,len(CurrentRanges_SamplesCount))):
        csv_string_list.append(f"{list_item[0]}-{list_item[-1]}, {CurrentRanges_SamplesCount[item]}")
    output_csv_string = "\n".join(csv_string_list)
    return output_csv_string
