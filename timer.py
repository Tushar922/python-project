# we will import required modules
from plyer import notification

# time module use unit second
import time

# set timer 3 hour 
timer=time.sleep(0)
print(timer)
# windows notification system in python
notification.notify(
title = "drink water",
message = "Hey drink some water",
timeout = 30 
)

# bye have a great day