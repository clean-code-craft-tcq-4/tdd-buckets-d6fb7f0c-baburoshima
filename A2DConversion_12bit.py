A2D_MAX_LIMIT_12Bit = 4094
A2D_MIN_LIMIT_12Bit = 0
MAX_AMPERE_READING_12Bit = 10

#-------------------Extension: Current-sensing at high fidelity---------------#

def Is_12bit_SensorInputOk(sensorReading):
    if sensorReading in range(A2D_MIN_LIMIT_12Bit,A2D_MAX_LIMIT_12Bit+1): #added one to include A2D_MAX_LIMIT in vailid range
        return True
    else:
        print("ERROR: Invalid sensor reading : ", sensorReading)
        return False

def Convert_12bit_to_Ampere(sensorReading):
    Ampere_Reading = round(MAX_AMPERE_READING_12Bit * sensorReading / A2D_MAX_LIMIT_12Bit)
    return Ampere_Reading










