# Controller for robot used to call correct functions from corresponding API
# Python 2/3 (Should work with both versions but check requirements of API/ required libraries)

# Import the API that should be used by the controller
# Syntax: from <api_file_name> import paul
from paul_pi import Paul

# Import time library
from time import time, sleep

# Instance of Paul class    
paul = Paul()

# Time step (in seconds)
# Use a sleep of at least 0.1, to avoid errors (This applies to Hardware implementations)
time_step = 0.2
# Max run time of the robot before termination (in seconds)
run_time = 20

# Used to stop the robot before the time is finished 
running = True

# Used to toggle displaying the readings from sensors and motors
display = False

# stores current direction & state
going_up = True

# Starting time of the robot (in seconds from epoch)
start_time = time()


#Turn the light on
#paul.light_on()
# Keep running the robot until it should stop or exceeds the run time
while(running and time() < start_time + run_time):
    try:
        increment = 5
        n = (int) (70/increment)
        value = increment
        for i in range(n):
            if(display):
                paul.display_all_readings()
            value += 5
            paul.start_motors(-value)
            sleep(time_step)
        # Pause the program for a set duration
        if(display):
            paul.display_all_readings()
        sleep(time_step)
    # Catch any exceptions that occure during execution 
    # these may affect the motors and lead to an unexpected termination of the loop
    # A I/O error can occur during while using the Raspberry Pi API (This is unavoidable and should be handled)
    except Exception as e:
        # Note: Below print statement will only work in Python2 
        print str(e)
        # Stop and restart the motors if an error occurs
        paul.start_motors(paul.get_speed())

# Tidy up - code to be executed before the script terminates
paul.paul_tidy()