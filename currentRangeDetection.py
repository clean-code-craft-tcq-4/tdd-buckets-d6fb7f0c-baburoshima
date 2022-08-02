MAX_LIMIT = 100
MIN_LIMIT = 0

def getcurrentvalues(CurrentSamples):
    if IsRangeOk(CurrentSamples):
        sorted_CurrentSamples = get_sorted_Samples(CurrentSamples)
        CurrentRanges_list = get_CurrentRangeslist(sorted_CurrentSamples)
        message = output_to_csv(CurrentRanges_list)
        print(message)
    else:
        return None
    return message

def IsRangeOk(values):
    for item in values:
        if item > MAX_LIMIT:
            return False
    return True

def get_sorted_Samples(CurrentSamples):
    sorted_array = sorted(CurrentSamples, reverse=False)
    return sorted_array

def get_CurrentRangeslist(sorted_CurrentSamples):
    interval = 1
    temp_arr = []
    CurrentRanges_list = []
    for index in range(0, len(sorted_CurrentSamples)):
        if (sorted_CurrentSamples[index] - sorted_CurrentSamples[index - interval] > interval):
            CurrentRanges_list.append(temp_arr)
            temp_arr = []
            temp_arr.append(sorted_CurrentSamples[index])
            continue
        else:
            temp_arr.append(sorted_CurrentSamples[index])
    CurrentRanges_list.append(temp_arr)
    return CurrentRanges_list


def output_to_csv(CurrentRanges_list):
    csv_string_list = []
    output_csv_string = ""
    csv_string_list.append(f"Range, Readings")
    for list_item in CurrentRanges_list:
        csv_string_list.append(f"{list_item[0]}-{list_item[-1]}, {len(list_item)}")
    output_csv_string = "\n".join(csv_string_list)
    return output_csv_string



getcurrentvalues([3, 3, 5, 4, 7,8, 10, 11,12])
getcurrentvalues([3, 3, 5, 4, 10, 11,12])
getcurrentvalues([4,5])
getcurrentvalues([3])
getcurrentvalues([5,6,6,7,1])