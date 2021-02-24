#Add Phidgets Library
from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
#Required for sleep statement
import time

#Create
servo = RCServo()

#Address
servo.setChannel(0)

#Open
servo.openWaitForAttachment(1000)

#Configure voltage based on servo attached (search datasheet online)
servo.setVoltage(RCServoVoltage.RCSERVO_VOLTAGE_6V)

#Initialize
servo.setTargetPosition(0)
servo.setEngaged(True)

working = True
while(working):
    targetPos = int(input("Enter number between 0-180. Enter -1 to exit\n"))
    if(targetPos >= 0):
        servo.setTargetPosition(targetPos)
    else:
        working = False

print("Program Exiting")
servo.close()
  