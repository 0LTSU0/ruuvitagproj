from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
from dbwriter import *


run_flag = RunFlag()
def handle_data(found_data):
    if found_data[0] == 'E5:87:D2:4F:69:5D':
        #print('Olohuone:', found_data[1])
        ruuvi_to_db("olohuone", found_data[1])
    elif found_data[0] == 'F9:E5:16:4C:AC:C1':
        #print('Makkari:', found_data[1])
        ruuvi_to_db("makkari", found_data[1])
    

if __name__ == '__main__':
    macs = ['E5:87:D2:4F:69:5D', 'F9:E5:16:4C:AC:C1'] #olohuone, makkari
    print("Starting ruuvitag data handler..")
    RuuviTagSensor.get_data(handle_data, macs, run_flag)
    