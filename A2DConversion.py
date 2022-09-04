#-------------------Extension:  10 and 12bit A2D converter --------------------------------------------#
#-------------------12 Bit :  Current-sensing at high fidelity-----------------------------------------#
#-------------------10 Bit : Sensor capable of detecting both charging and discharging currents--------#

A2D_MAX_LIMIT_10bit = 1022
A2D_MIN_LIMIT_10bit = 0
MAX_AMPERE_READING_10Bit = 15
A2D_MAX_LIMIT_12Bit = 4094
A2D_MIN_LIMIT_12Bit = 0
MAX_AMPERE_READING_12Bit = 10
POSITIVE_READINGS = "round(({2}*{0})/{1})"
POSITIVE_and_NEGATIVE_READINGS = "abs(round(({2}*2*{0}/{1})-{2}))"
A2D_converter = { 12 : (A2D_MIN_LIMIT_12Bit,A2D_MAX_LIMIT_12Bit,MAX_AMPERE_READING_12Bit,POSITIVE_READINGS),
                  10 : (A2D_MIN_LIMIT_10bit,A2D_MAX_LIMIT_10bit,MAX_AMPERE_READING_10Bit,POSITIVE_and_NEGATIVE_READINGS)}


def Is_SensorInputOk(sensorReading,A2Dbits):
    if sensorReading in range(A2D_converter[A2Dbits][0],A2D_converter[A2Dbits][1]+1) :#added one to include A2D_MAX_LIMIT in vailid range
        return True
    else:
        print("ERROR: Invalid sensor reading : ", sensorReading)
        return False

def Convert_Digital_to_Ampere(sensorReading,A2Dbits):
    Ampere_Reading = eval(A2D_converter[A2Dbits][3].format(sensorReading, A2D_converter[A2Dbits][1], A2D_converter[A2Dbits][2]))
    return Ampere_Reading






