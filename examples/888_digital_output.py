from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
import time

def main():
        digitalOutput0 = DigitalOutput()
        digitalOutput1 = DigitalOutput()
        digitalOutput2 = DigitalOutput()
        digitalOutput3 = DigitalOutput()
        digitalOutput4 = DigitalOutput()
        digitalOutput5 = DigitalOutput()
        digitalOutput6 = DigitalOutput()
        digitalOutput7 = DigitalOutput()

        digitalOutput0.setChannel(0)
        digitalOutput1.setChannel(1)
        digitalOutput2.setChannel(2)
        digitalOutput3.setChannel(3)
        digitalOutput4.setChannel(4)
        digitalOutput5.setChannel(5)
        digitalOutput6.setChannel(6)
        digitalOutput7.setChannel(7)

        digitalOutput0.openWaitForAttachment(5000)
        digitalOutput1.openWaitForAttachment(5000)
        digitalOutput2.openWaitForAttachment(5000)
        digitalOutput3.openWaitForAttachment(5000)
        digitalOutput4.openWaitForAttachment(5000)
        digitalOutput5.openWaitForAttachment(5000)
 digitalOutput6.openWaitForAttachment(5000)
        digitalOutput7.openWaitForAttachment(5000)

        digitalOutput0.setDutyCycle(1)
        digitalOutput1.setDutyCycle(1)
        digitalOutput2.setDutyCycle(1)
        digitalOutput3.setDutyCycle(1)
        digitalOutput4.setDutyCycle(1)
        digitalOutput5.setDutyCycle(1)
        digitalOutput6.setDutyCycle(1)
        digitalOutput7.openWaitForAttachment(5000)

        digitalOutput0.setDutyCycle(1)
        digitalOutput1.setDutyCycle(1)
        digitalOutput2.setDutyCycle(1)
        digitalOutput3.setDutyCycle(1)
        digitalOutput4.setDutyCycle(1)
        digitalOutput5.setDutyCycle(1)
        digitalOutput6.setDutyCycle(1)
        digitalOutput7.setDutyCycle(1)

        try:
                input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
                pass

        digitalOutput0.close()
        digitalOutput1.close()
        digitalOutput2.close()
        digitalOutput3.close()
        digitalOutput4.close()
        digitalOutput5.close()
        digitalOutput6.close()
        digitalOutput7.close()

main()

