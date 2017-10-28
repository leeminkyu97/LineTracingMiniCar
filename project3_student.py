import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

from ultraModule import getDistance

from TurnModule import *

from go_any import *

pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis = 20  # ??
obstacle = 1

# when obstacle=1, the power and
# running time of the first turn
SwingPr = 90  # student assignment (8)
SwingTr = 0.9  # student assignment (9)

try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        print('distance= ', distance)

        # when the distance is above the dis, moving object forwards
        if (distance > dis):
            go_forward_any(50)
            print('obstacle=', obstacle)

        # when the distance is below the dis, moving object stops
        if (distance <= dis):
            stop()
            print('stop')
            
        else:
            stop()
            sleep(1)


            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


except KeyboardInterrupt:
    pwm_low()
