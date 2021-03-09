from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.DigitalOutput import *
import time

#this is an even handler, when the readings from the channels change it will deal with them.
def IRonVoltageChange(self, voltage):
        print("State [" + str(self.getChannel()) + "]: " + str(state))

        #this will check that the voltage of the sensors is not above a threshold
        if(top_ds_reading >= 2.184 ):
            #stop motors as a voltage says we are 4cm from an object, until object is removed
        
        #could add more actions with other threshold values
        else:
            #continue

#this event handler will deal with the bumper switches input
def BSonStateChange(self, state):
        print("State [" + str(self.getChannel()) + "]: " + str(state))


        #this will check that the bumper switches have not hit anything
        if(state):
            #invert motors
        
        else:
            #continue

#defining array of digital inputs
digitalIN = [DigitalInput() for i in range (0,8)]
#addressing the channels
for i in range(0,8):
    digitalIN[i].setChannel(i)
    digitalIN[i].setOnStateChangeHandler(BSonStateChange)
    digitalIN[i].openWaitForAttachment(5000)

#defining array of analogue inputs

analogueIN = [VoltageInput() for i in range (0,8)]
#addressing the channels
for i in range(0,8):
    analogueIN[i].setChannel(i)
    
    #this line will basically call the event handler when the readings change
    analogueIN[i].setOnVoltageChangeHandler(IRonVoltageChange)
    analogueIN[i].openWaitForAttachment(5000)

#creating an average of the IR sensors
top_ds_reading = (analogueIN[0] + analogueIN[1] + analogueIN[2])/3

bottom_ds_reading = (analogueIN[3] + analogueIN[4] + analogueIN[5])/3
#closing channels
for i in range (0, 8):
    analogueIN[i].close()
    digitalIN[i].close()







