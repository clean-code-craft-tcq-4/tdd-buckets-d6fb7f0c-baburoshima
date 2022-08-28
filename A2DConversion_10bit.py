A2D_MAX_LIMIT_10bit = 1022
A2D_MIN_LIMIT_10bit = 0
MAX_POSSIBLE_READINGS = 15


#-------------------Extension: Sensor capable of detecting both charging and discharging currents---------------#

def Is_10bit_SensorInputOk(sensorReading):
    if sensorReading in range(A2D_MIN_LIMIT_10bit,A2D_MAX_LIMIT_10bit+1): #added one to include A2D_MAX_LIMIT in vailid range
        return True
    else:
        print("ERROR: Invalid sensor reading : ", sensorReading)
        return False

def Convert_10bit_to_Ampere(sensorReading):
    Ampere_Reading = abs(round((MAX_POSSIBLE_READINGS * 2 * sensorReading / A2D_MAX_LIMIT_10bit) - MAX_POSSIBLE_READINGS))
    print(Ampere_Reading)
    return Ampere_Reading








