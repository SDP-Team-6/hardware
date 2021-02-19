# API for Raspberry Pi Controller used to define Paul class
# Python 2 (Requirement for Motor Controllers)

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
        self.top_threshold = 10
        # Threshold reading on bottom distance sensors before triggering
        self.bottom_threshold = 10
        
        # Note: The following should only be set if distance sensors are not attached,
        # they should be set to 0 if sensors are attached.
        self.top_ds_reading = 20
        self.bottom_ds_reading = 20

        # Create an instance of the Motors class used in SDP
        self.mc = Motors()


# Movement Functions  

    def start_motors(self,speed):
        motor_ids = [5,4,3,2,1,0]
        self.speed = speed
        print 'Starting motors...'
        for motor_id in motor_ids:
            self.mc.move_motor(motor_id,self.speed)

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

    def check_top_ds_reading(self):
        return False 

    def display_top_ds_reading(self):
        print "Top DS Reading: --"
    

    def get_top_ds_reading(self):
        return self.top_ds_reading
    
    def check_bottom_ds_reading(self):
        return False 

    def display_bottom_ds_reading(self):
        print "Bottom DS Reading: --" 

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