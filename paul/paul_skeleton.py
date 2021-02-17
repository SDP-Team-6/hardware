# API for <insert_description> used to define Paul class
# Python 2/3 

# Imports go here

# Paul class is used to define a set of standard function calls (an API) to define how the controller interacts 
# with the enviroment (Webots, Hardware etc.)
class Paul(object):
    def __init__(self):
        # Name of the controller
        self.name = "PAUL controller for testing"

        # Current Speed of the robot (Used for excpetion handling recovery)
        # TODO Value required
        self.speed = None
        # Speed that the robot will travel up
        # TODO Value required
        self.up_speed = None
        # Speed that the robot will travel down
        # TODO Value required
        self.down_speed = None

        # Threshold reading on top distance sensors before triggering
        # TODO Value required
        self.top_threshold = None
        # Threshold reading on  distance sensors before triggering
        # TODO Value required
        self.bottom_threshold = None

        # Note: The following should only be set if distance sensors are not attached
        # they should be set to 0 if sensors are attached.
        # Reading value from the top distance sensor
        self.top_ds_reading = None
        # Reading value from the bottom distance sensor
        self.bottom_ds_reading = None


# Movement Functions   
    # Function to start the robot moving at a speed defined in the speed parameter
    def start_motors(self, speed):
        print 'Starting motors...'
        self.speed = speed
        # TODO Code goes below here

    # Function to stop the robot moving
    def stop_motors(self):
        print 'Stopping motors...'
        self.speed = 0
        # TODO Code goes below here


# Motors and Sensors Readings
    # Function to display all readings from the motors and sensors
    # If not required then dont add any code
    def display_all_readings(self):
        print ""        
        # TODO Code goes below here

    # Function to display any readings from the motors
    # Note: Not essential - can be left unchanged if not needed
    def display_motor_readings(self):
        # TODO Code goes below here
        print "Motor readings: "+str(self.speed)

    # Function get the current speed of the robot
    def get_motor_readings(self):
        # TODO Code goes below here
        return self.speed

    # Function to display any readings from the top distance sensor
    # Note: Not essential - can be left unchanged if not needed
    def display_top_ds_reading(self):
        # TODO Code goes below here
        print "Top DS Reading: " + str(self.top_ds_reading)

    # Function to display get readings from the top distance sensor
    def get_top_ds_reading(self):
        # TODO Code goes below here
        return self.top_ds_reading
    
    # Function to display any readings from the bottom distance sensor
    # Note: Not essential - can be left unchanged if not needed
    def display_bottom_ds_reading(self):
        # TODO Code goes below here
        print "Bottom DS Reading: " + str(self.bottom_ds_reading)

    # Function to display get readings from the bottom distance sensor
    def get_bottom_ds_reading(self):
        # TODO Code goes below here
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