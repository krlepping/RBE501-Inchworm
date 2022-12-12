"""MotorController controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
from controller import Manipulator
import math as math
from math import radians
from WebotsServoController import WebotsServoController
from Servo import Servo

#TIME_STEP = 64

class MotorController:
    def __init__(self):
        self.manipulator = Manipulator
        self.WebotsController = WebotsServoController()

        #joint_a = Servo(webots_servo=self.WebotsController.addServo("foot_ankle_joint2"))
        #joint_b = Servo(webots_servo=self.WebotsController.addServo("ankle_leg_joint2"))
        #joint_c = Servo(webots_servo=self.WebotsController.addServo("center_joint"))
        #joint_d = Servo(webots_servo=self.WebotsController.addServo("leg_ankle_joint1"))
        #joint_e = Servo(webots_servo=self.WebotsController.addServo("ankle_foot_joint1"))
        # get the motor devices
        joint_a = radians(robot.getDevice('foot_ankle_motor2'))
        joint_e= radians(robot.getDevice('foot_ankle_motor1'))
        joint_c = radians(robot.getDevice('center_motor'))
        joint_d = radians(robot.getDevice('ankle_leg_motor1'))
        joint_b= radians(robot.getDevice('ankle_leg_motor2'))
        
        self.Joints = [joint_a, joint_b, joint_c, joint_d, joint_e]

    def moveToPoint(self, x, y, z):
        joint_angles = self.manipulator.InchwormIK(x, y, z, self.Joints)
        
        
        # We can either stick this directly into webots, and it will go here based off the max speed the motors can go,
        # OR we make actual trajeectory planning
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    moveToPoint(4,5,7)
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
