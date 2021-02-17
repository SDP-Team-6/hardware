from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
import time

def onStateChange(self, state):
        print("State [" + str(self.getChannel()) + "]: " + str(state))

def main():
        digitalInput0 = DigitalInput()
        digitalInput1 = DigitalInput()
        digitalInput2 = DigitalInput()
        digitalInput3 = DigitalInput()
        digitalInput4 = DigitalInput()
        digitalInput5 = DigitalInput()
        digitalInput6 = DigitalInput()
        digitalInput7 = DigitalInput()

        digitalInput0.setChannel(0)
        digitalInput1.setChannel(1)
        digitalInput2 = DigitalInput()
        digitalInput3 = DigitalInput()
        digitalInput4 = DigitalInput()
        digitalInput5 = DigitalInput()
        digitalInput6 = DigitalInput()
        digitalInput7 = DigitalInput()

        digitalInput0.setChannel(0)
        digitalInput1.setChannel(1)
        digitalInput2.setChannel(2)
        digitalInput3.setChannel(3)
        digitalInput4.setChannel(4)
        digitalInput5.setChannel(5)
        digitalInput6.setChannel(6)
        digitalInput7.setChannel(7)

        digitalInput0.setOnStateChangeHandler(onStateChange)
        digitalInput1.setOnStateChangeHandler(onStateChange)
        digitalInput2.setOnStateChangeHandler(onStateChange)
        digitalInput3.setChannel(3)
        digitalInput4.setChannel(4)
        digitalInput5.setChannel(5)
        digitalInput6.setChannel(6)
        digitalInput7.setChannel(7)

        digitalInput0.setOnStateChangeHandler(onStateChange)
        digitalInput1.setOnStateChangeHandler(onStateChange)
        digitalInput2.setOnStateChangeHandler(onStateChange)
        digitalInput3.setOnStateChangeHandler(onStateChange)
        digitalInput4.setOnStateChangeHandler(onStateChange)
        digitalInput5.setOnStateChangeHandler(onStateChange)
        digitalInput6.setOnStateChangeHandler(onStateChange)
        digitalInput7.setOnStateChangeHandler(onStateChange)

        digitalInput0.openWaitForAttachment(5000)
        digitalInput1.openWaitForAttachment(5000)
        digitalInput2.openWaitForAttachment(5000)
        digitalInput3.openWaitForAttachment(5000)
        digitalInput4.setOnStateChangeHandler(onStateChange)
        digitalInput5.setOnStateChangeHandler(onStateChange)
        digitalInput6.setOnStateChangeHandler(onStateChange)
        digitalInput7.setOnStateChangeHandler(onStateChange)

        digitalInput0.openWaitForAttachment(5000)
        digitalInput1.openWaitForAttachment(5000)
        digitalInput2.openWaitForAttachment(5000)
        digitalInput3.openWaitForAttachment(5000)
        digitalInput4.openWaitForAttachment(5000)
        digitalInput5.openWaitForAttachment(5000)
        digitalInput6.openWaitForAttachment(5000)
        digitalInput7.openWaitForAttachment(5000)

        try:
                input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
                pass
        digitalInput0.close()
        digitalInput1.close()
        digitalInput2.close()
        digitalInput3.close()
        digitalInput4.close()
        digitalInput5.close()
        digitalInput6.close()
        digitalInput7.close()

main()

