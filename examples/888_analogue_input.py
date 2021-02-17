from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
import time

def onVoltageChange(self, voltage):
        print("Voltage [" + str(self.getChannel()) + "]: " + str(voltage))

def main():
        voltageInput0 = VoltageInput()
        voltageInput1 = VoltageInput()
        voltageInput2 = VoltageInput()
        voltageInput3 = VoltageInput()
        voltageInput4 = VoltageInput()
        voltageInput5 = VoltageInput()
        voltageInput6 = VoltageInput()
        voltageInput7 = VoltageInput()

        voltageInput0.setChannel(0)
        voltageInput1.setChannel(1)
        voltageInput2.setChannel(2)
        voltageInput3.setChannel(3)
        voltageInput4.setChannel(4)
        voltageInput5.setChannel(5)
        voltageInput6.setChannel(6)
        voltageInput7.setChannel(7)

        voltageInput0.setOnVoltageChangeHandler(onVoltageChange)
        voltageInput1.setOnVoltageChangeHandler(onVoltageChange)
        voltageInput2.setOnVoltageChangeHandler(onVoltageChange)
voltageInput3.setOnVoltageChangeHandler(onVoltageChange)
        voltageInput4.setOnVoltageChangeHandler(onVoltageChange)
        voltageInput5.setOnVoltageChangeHandler(onVoltageChange)
        voltageInput6.setOnVoltageChangeHandler(onVoltageChange)
        voltageInput7.setOnVoltageChangeHandler(onVoltageChange)

        voltageInput0.openWaitForAttachment(5000)
        voltageInput1.openWaitForAttachment(5000)
        voltageInput2.openWaitForAttachment(5000)
        voltageInput3.openWaitForAttachment(5000)
        voltageInput4.openWaitForAttachment(5000)
        voltageInput5.openWaitForAttachment(5000)
        voltageInput6.openWaitForAttachment(5000)
        voltageInput7.openWaitForAttachment(5000)

        try:
                input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
                pass
        voltageInput0.close()
        voltageInput1.close()
        voltageInput2.close()
        voltageInput3.close()
        voltageInput4.close()
        voltageInput5.close()
        voltageInput6.close()
        voltageInput7.close()

main()
