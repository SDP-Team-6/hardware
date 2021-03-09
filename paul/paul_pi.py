# API for Raspberry Pi Controller used to define Paul class
# Python 2 (Requirement for Motor Controllers)
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.DigitalOutput import *
import time
from motors import Motors

class Paul(object):
    def __init__(self):
        # Name of the controller
        self.name = "PAUL controller for Raspberry Pi"
        
        # Current Speed of the robot
        self.speed = 0
        # Speed that the robot will travel up (note negative speed goes up)
        self.up_speed = -100
        #Speed that the robot will travel down (note negative speed goes down)
        self.down_speed = 100
        
        # Threshold reading on top distance sensors before triggering
        self.top_threshold = 2.184
        # Threshold reading on bottom distance sensors before triggering
        self.bottom_threshold = 2.184
        
        # Note: The following should only be set if distance sensors are not attached,
        # they should be set to 0 if sensors are attached.
        self.top_ds_reading = 0
        self.bottom_ds_reading = 0

        # Create an instance of the Motors class used in SDP
        self.mc = Motors()

        #Sensors
        #define array of digital inputs to store readings from the bump sensors
        self.bump_sensors = [DigitalInput() for i in range (0,6)]
        #addressing the channels for the bump sensors
        #0-2 are top sensors
        #3-5 are bottom channels
        for i in range(0,6):
            self.bump_sensors[i].setChannel(i)
            self.bump_sensors[i].openWaitForAttachment(5000)

        #define array of analogue inputs to store readings from the ir sensors
        self.ir_sensors = [VoltageInput() for i in range (0,6)]
        #addressing the channels for the ir sensors
        #0-2 are top sensors
        #3-5 are bottom channels
        for i in range(0,6):
            self.ir_sensors[i].setChannel(i)
            #this line will basically call the event handler when the readings change
            self.ir_sensors[i].openWaitForAttachment(5000)


# Movement Functions  

    def start_motors(self,speed_input):
        #If speed_input is an int then the speeds of all the motors should be the same
        if type(speed_input) is int:
            speeds = [speed_input, speed_input, speed_input, speed_input, speed_input, speed_input]
            self.speed = speed_input
        #If speed_input is a list then the speeds should be set different, set speed to a non int value to disable changing speed on that motor
        elif type(speed_input) is list:
            speeds = speed_input
        #If list is not valid then set speeds to the current speed
        else:
            speeds = [self.speed, self.speed, self.speed, self.speed, self.speed, self.speed]
        #ID's of all the motors to run
        motor_ids = [5,4,3,2,1,0]
        print 'Starting motors...'
        #print speeds
        for i in range(len(speeds)):
        #for motor_id in motor_ids:
            if type(speeds[i]) is int:
                self.mc.move_motor(motor_ids[i],speeds[i])
            #self.mc.move_motor(motor_id,self.speed)

    def stop_motors(self):
        print 'Stopping motors...'
        self.speed = 0
        self.mc.stop_motors()


# Motors and Sensors Readings
    def display_all_readings(self):
        self.display_motor_readings()
        self.display_top_ds_reading()
        self.display_bottom_ds_reading()
        print ""
    
    def display_motor_readings(self):
        self.mc.print_encoder_data()
    
    def get_motor_readings(self):
        #mc.read_encoder(id)
        #where id is the port number on the encoder board that you wish to read
        return self.speed

    #Returns true if the top distance sensors are within range of the top 
    #Returns false otherwise
    def check_top_ds_reading(self):
        #Set the top distance sensor reading to the average of the three IR sensors on the top
        self.top_ds_reading = (self.ir_sensors[0].getVoltage() + self.ir_sensors[1].getVoltage() + self.ir_sensors[2].getVoltage())/3
        #If the voltage of the ir sensors is above a threshold then return true
        if(self.top_ds_reading >= self.top_threshold):
            return True
        #If any of the top bumper sensors have been activated then return true
        if(self.bump_sensors[0].getState() == 1 or self.bump_sensors[1].getState() == 1 or self.bump_sensors[2].getState() == 1):
            return True
        #Else return false
        return False 

    def display_top_ds_reading(self):
        print "Top DS Reading: " + str(self.top_ds_reading)
    

    def get_top_ds_reading(self):
        return self.top_ds_reading
    
    #Returns true if the top distance sensors are within range of the top 
    #Returns false otherwise
    def check_bottom_ds_reading(self):
        #Set the bottom distance sensor reading to the average of the three IR sensors on the bottom
        self.bottom_ds_reading = (self.ir_sensors[3].getVoltage() + self.ir_sensors[4].getVoltage() + self.ir_sensors[5].getVoltage())/3
        #If the voltage of the ir sensors is above a threshold then return true
        if(self.bottom_ds_reading >= self.bottom_threshold):
            return True
        #If any of the bottom bumper sensors have been activated then return true
        if(self.bump_sensors[3].getState() == 1 or self.bump_sensors[4].getState() == 1 or self.bump_sensors[5].getState() == 1):
            return True
        #Else return false
        return False 

    def display_bottom_ds_reading(self):
        print "Bottom DS Reading: " + str(self.bottom_ds_reading)

    def get_bottom_ds_reading(self):
        return self.bottom_ds_reading


# Terminate script
    def paul_tidy(self):
        #Stop the motors
        self.stop_motors()
        
        #Keyboard inerrupt may be needed to reset phidget
        #try:
        #    input("Press Enter to Stop\n")
        #except (Exception, KeyboardInterrupt):
        #    pass

        #Close all the channels
        for i in range (0, 6):
            self.ir_sensors[i].close()
            self.bump_sensorss[i].close()



# Getters and Setters

    def get_name(self):
        return self.name
    
    def set_speed(self,name):
        self.name = name

    def get_speed(self):
        return self.speed
    
    def set_speed(self,speed):
        self.speed = speed
    
    def get_up_speed(self):
        return self.up_speed
    
    def set_up_speed(self,up_speed):
        self.up_speed = up_speed
    
    def get_down_speed(self):
        return self.down_speed
    
    def set_down_speed(self,up_speed):
        self.down_speed = up_speed

    def get_top_threshold(self):
        return self.top_threshold
    
    def set_top_threshold(self,top_threshold):
        self.top_threshold = top_threshold

    def get_bottom_threshold(self):
        return self.bottom_threshold

    def set_bottom_threshold(self,bottom_threshold):
        self.bottom_threshold = bottom_threshold