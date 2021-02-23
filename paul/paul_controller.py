# Controller for robot used to call correct functions from corresponding API
# Python 2/3 (Should work with both versions but check requirements of API/ required libraries)

# Import the API that should be used by the controller
# Syntax: from <api_file_name> import paul
from paul_webots import Paul

# Import time library
from time import time, sleep

# Instance of Paul class
paul = Paul()

# Time step (in seconds)
# Use a sleep of at least 0.1, to avoid errors (This applies to Hardware implementations)
time_step = 0.2
# Max run time of the robot before termination (in seconds)
run_time = 10

# Used to stop the robot before the time is finished
running = True

# Used to toggle displaying the readings from sensors and motors
display = False

# stores current direction & state
going_up = True

# Starting time of the robot (in seconds from epoch)
start_time = time()

# Start the robot moving up the pole
paul.start_motors(paul.get_up_speed())

paul.run(display, going_up, running, time_step, start_time, run_time)
