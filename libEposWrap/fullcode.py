# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import math
import RPi.GPIO as GPIO
import json

import ctypes
import constants
import DriveTrain
import helperFunctions as hF


# Import the PCA9685 module.
import Adafruit_PCA9685

import serial


ser = serial.Serial('/dev/ttyACM0',9600)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]

state = 0
doMovement = 'FORWARD'

#Encoder units per rotation
MODVALUE = 175619;

pi = 3.14159265;
START_OFFSET_ANGLE = pi/2.0;

def getGroundSpeed(airSpeed):
    return int(legAirSpeed *(2*landingAngle/(2*pi - 2*landingAngle)));

legAirSpeed = int(2.0*600);
landingAngle = 0.349;
legGroundSpeed = getGroundSpeed(legAirSpeed);
PROFILE_POSITION_MODE = 1

FRONTLEFT   = 1;
MIDDLELEFT  = 2;
BACKLEFT    = 3;
FRONTRIGHT  = 4;
MIDDLERIGHT = 5;  
BACKRIGHT   = 6;
accel = 20000;
deccel = 20000;

tolerance = 30000

lastGoalPosArray = [0]*6;
firstMovement = True

def getMoveCommandInfo(curMovement, state):
    global pi, landingAngle, legAirSpeed, legGroundSpeed
    a = 2*pi - landingAngle
    b = landingAngle
    air = legAirSpeed
    ground = legGroundSpeed

    if curMovement == 'STANDUP':
        goClockwises = [True, True, True, True, True, True]
        legAngles = [0, 0, 0, 0, 0, 0]
        legSpeeds = [air, air, air, air, air, air]
    elif curMovement == 'FORWARD':
        goClockwises = [True, True, True, True, True, True]
        if state == 1:
            legAngles = [b, a, b, a, b, a]
            legSpeeds = [ground, air, ground, air, ground, air]
        elif state == 2:
            legAngles = [a, b, a, b, a, b]
            legSpeeds = [air, ground, air, ground, air, ground]
    elif curMovement == 'BACKWARD':
        goClockwises = [False, False, False, False, False, False]
        if state == 1:
            legAngles = [a, b, a, b, a, b]
            legSpeeds = [ground, air, ground, air, ground, air]
        elif state == 2:
            legAngles = [b, a, b, a, b, a]
            legSpeeds = [air, ground, air, ground, air, ground]

    elif curMovement == 'ROTATECLOCKWISE': 
        goClockwises = [True, True, True, False, False, False]
        if (state == 1):
            legAngles = [b, a, b, b, a, b]
            legSpeeds = [ground, air, ground, air, ground, air]
        elif (state == 2):
            legAngles = [a, b, a, a, b, a]
            legSpeeds = [air, ground, air, ground, air, ground]

    elif curMovement == 'ROTATECOUNTERCLOCKWISE': 
        goClockwises = [False, False, False, True, True, True]
        if (state == 1):
            legAngles = [a, b, a, a, b, a]
            legSpeeds = [ground, air, ground, air, ground, air]
        elif (state == 2):
            legAngles = [b, a, b, b, a, b]
            legSpeeds = [air, ground, air, ground, air, ground]
    elif curMovement == 'STOP':
        goClockwises = [False, False, False, True, True, True]
        if (state == 1):
            legAngles = [a, b, a, a, b, a]
            legSpeeds = [0, 0, 0, 0, 0, 0]
        elif (state == 2):
            legAngles = [b, a, b, b, a, b]
            legSpeeds = [0, 0, 0, 0, 0, 0]       
    # setup object
    m = {}
    m["legAngles"] = legAngles
    m["legSpeeds"] = legSpeeds
    m["goClockwises"] = goClockwises

    return m


def getSetupInfo(curMovement, curPos):
    global pi, landingAngle, legAirSpeed, legGroundSpeed
    a = 2*pi - landingAngle
    b = landingAngle
    air = legAirSpeed
    ground = legGroundSpeed

    if curMovement == 'FORWARD':
        goClockwises = [True, True, True, True, True, True]
        legAngles = [a, b, a, b, a, b]
        legSpeeds = [air, air, air, air, air, air]
    elif curMovement == 'BACKWARD':
        goClockwises = [False, False, False, False, False, False]
        legAngles = [b, a, b, a, b, a]
        legSpeeds = [air, air, air, air, air, air]
    elif curMovement == 'ROTATECLOCKWISE':
        goClockwises = [True, True, True, False, False, False]
        legAngles = [a, b, a, a, b, a]
        legSpeeds = [air, ground, air, ground, air, ground]
    elif curMovement == 'ROTATECOUNTERCLOCKWISE':
        goClockwises = [False, False, False, True, True, True]
        legAngles = [b, a, b, b, a, b]
        legSpeeds = [air, ground, air, ground, air, ground]
    elif curMovement == 'STOP':
        goClockwises = [False, False, False, True, True, True]
        legAngles = [b, a, b, b, a, b]
        legSpeeds = [0, 0, 0, 0, 0, 0]
    # setup object
    m = {}
    m["legAngles"] = legAngles
    m["legSpeeds"] = legSpeeds
    m["goClockwises"] = goClockwises

    return m

# Move legs function implemented in python
def moveLegs(goalAngles, vels, goClockwises, driveTrain):
    global pi, landingAngle, legAirSpeed, legGroundSpeed, lastGoalPosArray, firstMovement
    
    # set legs to specified position profile
    for i in range(6):
        driveTrain.setPositionProfile(i + 1, vels[i], accel,deccel);

    # Need to get current positions in order to calculate goal position in maxon coordinates.
    # Convert to goal position in maxon coordinates using current position (maxon coordinates)
    # and the goalAngle (radians)
    curPosArray = []
    goalPosArray = []

    # If it's the first time the legs have been moved, get their actual positions
    if firstMovement:
        for i in range(6):
            curPosArray.append(driveTrain.getPosition(i + 1));
            goalPosArray.append(driveTrain.getGoalPos(i + 1, curPosArray[i], goalAngles[i], goClockwises[i]))
            firstMovement = False
    else:
        for i in range(6):
            curPosArray.append(lastGoalPosArray[i]);
            goalPosArray.append(driveTrain.getGoalPos(i + 1, curPosArray[i], goalAngles[i], goClockwises[i]))


        # Store last goal positions
    lastGoalPosArray = goalPosArray;

    # set the position
    for i in range(6):
        driveTrain.setPosition(i + 1, goalPosArray[i], True);


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)



def getCommands(intArray): # this is not used
    COMMANDS["wristTilt"] = intArray[0]
    COMMANDS["wristPan"] = intArray[1]
    COMMANDS["l1Theta"] = intArray[2]
    COMMANDS["l2Theta"] = intArray[3]
    COMMANDS["continuous"] = intArray[4]
    COMMANDS["claw"] = intArray[5]
    COMMANDS["camera1Pan"] = intArray[6]
    COMMANDS["camera1Tilt"] = intArray[7]
    return COMMANDS

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


# GET PINS
(CONTINUOUSPIN, L1PIN, L2PIN, WRISTPANPIN, WRISTTILTPIN, CAMERA1PANPIN, CAMERA1TILTPIN) = (0,1,2,3,4,5,6)

COMMANDS = {}

# --------- MOTOR SETUP ------------
#Declare new drive train object. The constructor accepts a USB port name as a string
#USB0 is typically the device that the motor controller connects to
driveTrain = DriveTrain.EposDriveTrain()
print("Initializing...")

#Initialize drive train object
#Note: this object must be initialized by calling init() before trying to move any motors!
driveTrain.init()

#Enable all nodes, and clear any faults
#Note: before a motor can be moved, it must be enabled!
driveTrain.enableAll()
driveTrain.clearAllFaults()

#Set the i-th node to appropriate mode
for i in range(6):
    driveTrain.setMode(i + 1, PROFILE_POSITION_MODE)
# ----------------------------------


# STANDUP ROVER
m = getMoveCommandInfo('STANDUP', 1)
moveLegs(m["legAngles"], m["legSpeeds"], m["goClockwises"], driveTrain)


# flag for making sure state is only called once
moveCommandFlag = True


while True:
    commands=[]
    read_serial=ser.readline()
    if len(read_serial.split("-")) > 1:
        commands = read_serial.split("-")
        legAirSpeed, angle = int(float(commands[1].strip('\t\n\r')))
        legGroundSpeed = getGroundSpeed(legAirSpeed)
        direction = commands[0].strip('\t\n\r')
    
    # print('dir' + direction )
    # print(' angle: S' + str(angle))
    # if direction == "x":
    #     pwm.set_pwm(L1PIN, 0, angle)
    #     pwm.set_pwm(CONTINUOUSPIN, 0, 0)
    # elif direction == "c":
    #     pwm.set_pwm(L2PIN, 0, angle)
    #     pwm.set_pwm(CONTINUOUSPIN, 0, 0)
    # elif direction == "z":
    #     pwm.set_pwm(CONTINUOUSPIN, 0, angle)
    # else:
    #     pwm.set_pwm(CONTINUOUSPIN, 0, 0)

    CONTINUOUSSERVOSTOPVALUE = 140
    if direction == "w":
            doMovement = 'FORWARD'
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE) 
    elif direction == "s":
            doMovement = 'BACKWARD'
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "a":
            doMovement = 'ROTATECOUNTERCLOCKWISE'
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "d":
            doMovement = 'ROTATECLOCKWISE'
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "x":
            doMovement = 'STOP'
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "c": # arm control mode (next 5 cases) case 1-4 servos in arm, 5 is gripper 
            doMovement = 'STOP' #(linear a)
            if(angle > 475): # hard check to make sure it doesn't break stuff
                angle = 475
            elif(angle < 275):
                angle = 275
            pwm.set_pwm(L1PIN, 0, angle)
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "v": #linear actuator 2 (smaller one)
            doMovement = 'STOP'
            if(angle > 475):  
                angle = 475
            elif(angle < 275):
                angle = 275
            pwm.set_pwm(L2PIN, 0, angle)
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "b": #rotate base motor
            doMovement = 'STOP'
            if(angle > 225):  
                angle = 225
            elif(angle < 100):
                angle = 100
            pwm.set_pwm(CONTINUOUSPIN, 0, angle)
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)
    elif direction == "n": #wrist tilt
            doMovement = 'STOP'
            if(angle > 520):  
                angle = 520
            elif(angle < 150):
                angle = 100
            pwm.set_pwm(wristTilt, 0, angle)
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE) 
    elif direction == "m": #wrist tilt
            doMovement = 'STOP'
            if(angle > 520):  
                angle = 520
            elif(angle < 150):
                angle = 100
            pwm.set_pwm(wristPan, 0, angle) 
            pwm.set_pwm(CONTINUOUSPIN, 0, CONTINUOUSSERVOSTOPVALUE)                        
    # -----STATE MACHINE--------
    # state 0 setups rover to new doMovement command depending on current configuration
    if state == 0:
        # stateCommandCalled is meant so that moveRightLegs and moveLeftLegs are only called once per state
        if moveCommandFlag:
            curPos = [driveTrain.getPosition(legID) for legID in range(1,7)]
            m = getSetupInfo(doMovement, curPos)
            if doMovement != 'STOP':
                moveLegs(m["legAngles"], m["legSpeeds"], m["goClockwises"], driveTrain)

        if moveCommandFlag:
            moveCommandFlag = False
        
        if driveTrain.areAllCloseEnough(tolerance):
            state = 1
            moveCommandFlag = True

    # move right feet through air and move left feet on ground
    elif state == 1:
        if moveCommandFlag:
            m = getMoveCommandInfo(doMovement, 1)
            if doMovement != 'STOP':
                moveLegs(m["legAngles"], m["legSpeeds"], m["goClockwises"], driveTrain)
        
        if moveCommandFlag:
            moveCommandFlag = False
               
        if driveTrain.areAllCloseEnough(tolerance):
            state = 2
            moveCommandFlag = True
        

    # move left feet through air and move left feet on ground
    elif state == 2:
        if moveCommandFlag:
            m = getMoveCommandInfo(doMovement, 2)
            if doMovement != 'STOP':
                moveLegs(m["legAngles"], m["legSpeeds"], m["goClockwises"], driveTrain)

        if moveCommandFlag:
            moveCommandFlag = False
          
        if driveTrain.areAllCloseEnough(tolerance):
            state = 1
            moveCommandFlag = True










