from paul_testing import Paul
from time import time, ctime, sleep

# Instance of Paul class    
paul = Paul()

# Time step (in seconds)
time_step = 0.2
# Max run time of the robot before termination (in seconds)
run_time = 10

# Used to stop the robot before the time is finished 
running = True

# stores current direction & state
goingUp = True

# Starting time of the robot (in seconds from epoch)
start_time = time()

paul.start_motors(paul.get_up_speed())
while(running and time() < start_time + run_time):
    try:
        paul.display_all_readings()

        # if going up
        if goingUp:
            if paul.get_top_ds_reading() < paul.get_top_threshold():
                # reaching ceiling, stop
                goingUp = False
                paul.stop_motors()
                paul.start_motors(paul.get_down_speed())
    
        # if going down
        elif not goingUp:
            if paul.get_bottom_ds_reading() < paul.get_bottom_threshold():
                # reaching floor, stop
                goingUp = True
                paul.stop_motors()
                paul.start_motors(paul.get_up_speed())
        else:
            paul.stop_motors()
            running = False

        sleep(time_step)

    except Exception, e:
        print str(e)
        # Stop and restart the motors if an error occurs
        paul.stop_motors()
        paul.start_motors(paul.get_speed())

# Tidy up
paul.stop_motors()