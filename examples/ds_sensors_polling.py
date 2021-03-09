from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.DigitalOutput import *
from time import time, sleep

#defining array of analogue inputs
analogueIN = [VoltageInput() for i in range (0,6)]
digitalIN = [DigitalInput() for i in range (0,6)]

for i in range(0,6):
    digitalIN[i].setChannel(i)
    digitalIN[i].openWaitForAttachment(5000)


#addressing the channels
for i in range(0,6):
    analogueIN[i].setChannel(i)
    analogueIN[i].openWaitForAttachment(5000)
    
    #this line will basically call the event handler when the readings change

#creating an average of the IR sensors
t = 0
while(t < 5):
    print t
    for i in range (0, 6):
        print "IR State [" + str(i) + "]: " + str(analogueIN[i].getVoltage())
        #print analogueIN[i].getVoltage() < 2
    for i in range (0, 6):
        print "BS State [" + str(i) + "]: " + str(digitalIN[i].getState())
        #print digitalIN[i].getState() == 1
    t = t+1
    sleep(0.2)
    
        
#try:
    #input("Press Enter to Stop\n")
#except (Exception, KeyboardInterrupt):
    #pass
#closing channels
for i in range (0, 6):
    digitalIN[i].close()
    analogueIN[i].close()