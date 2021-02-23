# API for Webots used to define Paul class
# Python 3

# Imports go here
from controller import Robot, Motor, DistanceSensor

# Paul class is used to define a set of standard function calls (an API) to define how the controller interacts
# with the enviroment (Webots, Hardware etc.)
class Paul(object):
    def __init__(self):
        # Name of the controller
        self.name = "PAUL controller for Webots"

        # Current Speed of the robot (Used for excpetion handling recovery)
        # TODO Value required
        self.speed = 0
        # Speed that the robot will travel up
        # TODO Value required
        self.up_speed = 5
        # Speed that the robot will travel down
        # TODO Value required
        self.down_speed = -5

        # Threshold reading on top distance sensors before triggering
        # TODO Value required
        self.top_threshold = 1000
        # Threshold reading on  distance sensors before triggering
        # TODO Value required
        self.bottom_threshold = 1000

        # create the Robot instance.
        self.robot = Robot()

        # get the time step of the current world.
        self.timestep = int(self.robot.getBasicTimeStep())

        # initialise the 3 wheels
        self.wheels = []
        wheelsNames = ['wheel1', 'wheel2', 'wheel3']
        for i in range(3):
            self.wheels.append(self.robot.getDevice(wheelsNames[i]))
            self.wheels[i].setPosition(float('inf'))
            self.wheels[i].setVelocity(0.0) # unit: rad/s
        # initialise distance sensors
        self.ds_top = self.robot.getDevice('ds_top')
        self.ds_bottom = self.robot.getDevice('ds_bottom')
        self.ds_top.enable(self.timestep)
        self.ds_bottom.enable(self.timestep)
        # initialise LED
        # self.uv_led = self.robot.getDevice('uv_led')

# Movement Functions
    # Function to start the robot moving at a speed defined in the speed parameter
    def start_motors(self, speed):
        print("Starting motors...")
        self.speed = speed
        for i in range(3):
            self.wheels[i].setVelocity(speed)

    # Function to stop the robot moving
    def stop_motors(self):
        print("Stopping motors...")
        self.speed = 0
        for i in range(3):
            self.wheels[i].setVelocity(0)

# Motors and Sensors Readings
    # Function to display all readings from the motors and sensors
    # If not required then dont add any code
    def display_all_readings(self):
        display_motor_readings()
        display_top_ds_reading()
        display_bottom_ds_reading()

    # Function to display any readings from the motors
    # Note: Not essential - can be left unchanged if not needed
    def display_motor_readings(self):
        # TODO Code goes below here
        print("Motor speed: " + str(self.wheels[0].getVelocity()))

    # Function get the current speed of the robot
    def get_motor_readings(self):
        # TODO Code goes below here
        return self.wheels[0].getVelocity()

    # Function to check if the top distance sensor reading is within the threshold to trigger a change in direction
    # Returns True if the distance should change
    # Returns False if the distance is not within the threshold
    def check_top_ds_reading(self):
        return self.get_top_ds_reading() < self.get_top_threshold()

    # Function to display any readings from the top distance sensor
    # Note: Not essential - can be left unchanged if not needed
    def display_top_ds_reading(self):
        # TODO Code goes below here
        print("Top DS Reading: " + str(get_top_ds_reading()))

    # Function to display get readings from the top distance sensor
    def get_top_ds_reading(self):
        # TODO Code goes below here
        return self.ds_top.getValue()

    # Function to check if the top distance sensor reading is within the threshold to trigger a change in direction
    # Returns True if the distance should change
    # Returns False if the distance is not within the threshold
    def check_bottom_ds_reading(self):
        return self.get_bottom_ds_reading() < self.get_bottom_threshold()

    # Function to display any readings from the bottom distance sensor
    # Note: Not essential - can be left unchanged if not needed
    def display_bottom_ds_reading(self):
        # TODO Code goes below here
        print("Bottom DS Reading: " + str(self.get_bottom_ds_reading()))

    # Function to display get readings from the bottom distance sensor
    def get_bottom_ds_reading(self):
        # TODO Code goes below here
        return self.ds_bottom.getValue()


# Getters and Setters
    def get_name(self):
        return self.name

    def set_name(self,name):
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

    def set_down_speed(self,down_speed):
        self.down_speed = down_speed

    def get_top_threshold(self):
        return self.top_threshold

    def set_top_threshold(self,top_threshold):
        self.top_threshold = top_threshold

    def get_bottom_threshold(self):
        return self.bottom_threshold

    def set_bottom_threshold(self,bottom_threshold):
        self.bottom_threshold = bottom_threshold


# Run
    def run(self, display, going_up, running, time_step, start_time, run_time):
        while self.robot.step(self.timestep) != -1:
            try:
                # If the display option is enabled display all readings as defined in the API
                if(display):
                    self.display_all_readings()

                # If the robot is moving up the pole
                if going_up:
                    # Check that the robot has gone past the distance sensor stopping threshold
                    if self.check_top_ds_reading():
                        # If the robot has reached the ceiling the move the robot down
                        goingUp = False
                        self.stop_motors()
                        self.start_motors(self.get_down_speed())

                # If the robot is moving down the pole
                elif not going_up:
                    if self.check_bottom_ds_reading():
                        # If the robot has reached the floor then move the robot back up
                        goingUp = True
                        self.stop_motors()
                        self.start_motors(self.get_up_speed())
                else:
                    # If there the robot is not moving up or down then there is an issue and the code should be terminated
                    self.stop_motors()

            # Catch any exceptions that occure during execution
            # these may affect the motors and lead to an unexpected termination of the loop
            # A I/O error can occur during while using the Raspberry Pi API (This is unavoidable and should be handled)
            except Exception as e:
                # Note: Below print statement will only work in Python2
                #print str(e)
                # Stop and restart the motors if an error occurs
                paul.stop_motors()
                paul.start_motors(paul.get_speed())
