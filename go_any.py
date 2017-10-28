import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)


def REVERSE(x):
   if x == 'True': 
      return 'False'
   elif x == 'False': 
      return 'True'


forward0 = 'True'
forward1 = 'False'

backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)


MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


def leftmotor(x):
        if x == 'True':
                GPIO.output(MotorLeft_A, GPIO.HIGH)
                GPIO.output(MotorLeft_B, GPIO.LOW)
        elif x == 'False':
                GPIO.output(MotorLeft_A, GPIO.LOW)
                GPIO.output(MotorLeft_B, GPIO.HIGH)
        else:
                print 'Config Error'

def rightmotor(x):
        if x == 'True':
                GPIO.output(MotorRight_A, GPIO.LOW)
                GPIO.output(MotorRight_B, GPIO.HIGH)
        elif x == 'False':
                GPIO.output(MotorRight_A, GPIO.HIGH)
                GPIO.output(MotorRight_B, GPIO.LOW)


GPIO.setup(MotorLeft_A,GPIO.OUT)
GPIO.setup(MotorLeft_B,GPIO.OUT)
GPIO.setup(MotorLeft_PWM,GPIO.OUT)

GPIO.setup(MotorRight_A,GPIO.OUT)
GPIO.setup(MotorRight_B,GPIO.OUT)
GPIO.setup(MotorRight_PWM,GPIO.OUT)


LeftPwm=GPIO.PWM(MotorLeft_PWM,100)
RightPwm=GPIO.PWM(MotorRight_PWM,100)

def go_forward_any(speed):
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

def go_backward_any(speed):
    leftmotor(backward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(backward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

def go_forward(speed, running_time):
    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def go_backward(speed, running_time):
    leftmotor(backward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    rightmotor(backward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def stop():
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)

def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)

def pwm_low():
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()

