from __future__ import print_function
import time
from pololu_drv8835_rpi import motors, MAX_SPEED
import web
import RPi.GPIO as GPIO
import pygame

diodesGpio = [20,21,17,26,16,18,27,24]
GPIO.setmode(GPIO.BCM)

speed_up_forward = list(range(0, MAX_SPEED, 1))
slow_down_forward = list(range(MAX_SPEED, 0, -1)) + [0]
SPEED = 200;


def lightDiodes(gpio1, gpio2):
    GPIO.setmode(GPIO.BCM)
    turnOnGpio(gpio1)
    turnOnGpio(gpio2)

def turnOffDiodes(gpio1, gpio2):
    GPIO.setmode(GPIO.BCM)
    turnOffGpio(gpio1)
    turnOffGpio(gpio2)

def turnOnGpio(number):
    GPIO.setup(number, GPIO.OUT)
    GPIO.output(number, True)

def turnOffGpio(number):
    GPIO.setup(number, GPIO.OUT)
    GPIO.output(number, False)
    


urls = (
    '/', 'index',
    '/forward', 'forward',
    '/left', 'left',
    '/right', 'right',
    '/back', 'back',
    '/stop','stop',
    '/leftforward','leftforward',
    '/rightforward','rightforward',
    '/lightson','lightson',
    '/lightsoff','lightsoff',
    '/play','play'
)

class index:
    def GET(self):
        return "Welcome to raspberry pi controller"

class forward:
    def GET(self):
        try:
            motors.setSpeeds(0, 0)
            motors.motor1.setSpeed(SPEED)
            motors.motor2.setSpeed(SPEED)
    

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class left:
    def GET(self):
        try:
            motors.setSpeeds(0, 0)
            motors.motor1.setSpeed(-SPEED)
            motors.motor2.setSpeed(SPEED)
    

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class right:
    def GET(self):
        try:
            motors.setSpeeds(0, 0)
            motors.motor1.setSpeed(SPEED)
            motors.motor2.setSpeed(-SPEED)
    

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class back:
    def GET(self):
        lightDiodes(diodesGpio[0], diodesGpio[1])
        try:
            motors.setSpeeds(0, 0)
            motors.motor1.setSpeed(-SPEED)
            motors.motor2.setSpeed(-SPEED)
            

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class stop:
    def GET(self):
        try:
            motors.setSpeeds(0, 0)
            turnOffDiodes(diodesGpio[0], diodesGpio[1])
            #GPIO.cleanup()

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class leftforward:
    def GET(self):
        try:
            motors.setSpeeds(0, 0)
            motors.motor1.setSpeed(SPEED/2)
            motors.motor2.setSpeed(SPEED)
    

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class rightforward:
    def GET(self):
        try:
            motors.setSpeeds(0, 0)
            motors.motor1.setSpeed(SPEED)
            motors.motor2.setSpeed(SPEED/2)
    

        except:
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
            motors.setSpeeds(0, 0)
        return "going forward"

class lightson:
    def GET(self):
        try:
            lightDiodes(diodesGpio[2],diodesGpio[3])
            lightDiodes(diodesGpio[4],diodesGpio[5])
            lightDiodes(diodesGpio[6],diodesGpio[7])
        except:
            GPIO.cleanup()
        return "going forward"

class lightsoff:
    def GET(self):
        try:
            turnOffDiodes(diodesGpio[2],diodesGpio[3])
            turnOffDiodes(diodesGpio[4],diodesGpio[5])
            turnOffDiodes(diodesGpio[6],diodesGpio[7])    
        except:
            GPIO.cleanup()
            # Stop the motors, even if there is an exception
            # or the user presses Ctrl+C to kill the process.
        return "going forward"

class play:
    def GET(self):
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/iamrobot.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        return "going forward"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
