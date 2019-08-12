import random
import time

NORMAL_READING = 100
ODD_READING = 500

def generateSensorData(): 
    if (random.randrange(0, 5) == 0): 
        return ODD_READING
    else: 
        return NORMAL_READING

def poolSensorData(rate,format=0):
    while(True):
        var = generateSensorData()
        if(format != 0):
            if(var==ODD_READING):
                print("Alert !! Abnormal Reading.")
        else:
            print(var)        
        time.sleep(rate) 

# Driver code 
poolSensorData(1,1)