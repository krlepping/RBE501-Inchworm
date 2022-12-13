import Manipulator
import math as math
from math import radians
from WebotsServoController import WebotsServoController
from Servo import Servo
from controller import Robot, Motor

#TIME_STEP = 64

# create the Robot instance.
robot = Robot()



class MotorController:
    def __init__(self):
        self.manipulator = Manipulator()
        self.WebotsController = WebotsServoController()

        #joint_a = Servo(webots_servo=self.WebotsController.addServo("foot_ankle_joint2"))
        #joint_b = Servo(webots_servo=self.WebotsController.addServo("ankle_leg_joint2"))
        #joint_c = Servo(webots_servo=self.WebotsController.addServo("center_joint"))
        #joint_d = Servo(webots_servo=self.WebotsController.addServo("leg_ankle_joint1"))
        #joint_e = Servo(webots_servo=self.WebotsController.addServo("ankle_foot_joint1"))
        # get the motor devices
        joint_a = robot.getDevice('foot_ankle_motor2')
        joint_e = robot.getDevice('foot_ankle_motor1')
        joint_c = robot.getDevice('center_motor')
        joint_d = robot.getDevice('ankle_leg_motor1')
        joint_b = robot.getDevice('ankle_leg_motor2')
        
        self.Joints = [joint_a, joint_b, joint_c, joint_d, joint_e]

    def whereAt(self):
        position = self.manipulator.InchwormFK(self.Joints)
        print(f"{position}")
        return position


    def moveToPoint(self, x, y, z):
        joint_angles = self.manipulator.InchwormIK(x, y, z, self.Joints)
        print(f"{joint_angles}")
        return joint_angles
        
        
        # We can either stick this directly into webots, and it will go here based off the max speed the motors can go,
        # OR we make actual trajeectory planning

