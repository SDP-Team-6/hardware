from time import time, ctime, sleep
class Paul(object):
    def __init__(self):
        # Name of the controller
        self.name = "PAUL controller for testing"

        # Current Speed of the robot (Used for excpetion handling recovery)
        self.speed = 0
        # Speed that the robot will travel up
        self.up_speed = -100
        # Speed that the robot will travel down
        self.down_speed = 100

        # Threshold reading on top distance sensors before triggering
        self.top_threshold = 10
        # Threshold reading on  distance sensors before triggering
        self.bottom_threshold = 10

        # Note: The following are not needed for non-testing controllers
        self.top_ds_reading = 20
        self.bottom_ds_reading = 20

# Movement Functions   
    
    def start_motors(self,speed):
        print 'Starting motors...'
        self.speed = speed

    def stop_motors(self):
        print 'Stopping motors...'

# Motors and Sensors Readings
    def display_all_readings(self):
        print(ctime())
        self.display_motor_readings()
        self.display_top_ds_reading()
        self.display_bottom_ds_reading()
        print ""

    def display_motor_readings(self):
        print "Motor readings: "+str(self.speed)

    def get_motor_readings(self):
        return self.speed

    def display_top_ds_reading(self):
        print "Top DS Reading:" + str(self.top_ds_reading)

    def get_top_ds_reading(self):
        return self.top_ds_reading

    def display_bottom_ds_reading(self):
        print "Bottom DS Reading: " + str(self.bottom_ds_reading)

    def get_bottom_ds_reading(self):
        return self.bottom_ds_reading

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