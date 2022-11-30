import Manipulator
import math as math
from WebotsServoController import WebotsServoController
from Servo import Servo

class MotorController:
    def __init__(self):
        # self.motor1 = [-math.pi, math.pi] # These probably aren't needed as the Webots servos should carry all this info
        # self.motor2 = [-math.pi, math.pi]
        # self.motor3 = [-math.pi, math.pi]
        # self.motor4 = [-math.pi, math.pi]
        # self.motor5 = [-math.pi, math.pi]
        self.manipulator = Manipulator
        self.WebotsController = WebotsServoController()

        joint_a = Servo(webots_servo=self.WebotsController.addServo("Need Names Here"))
        joint_b = Servo(webots_servo=self.WebotsController.addServo("Need Names Here"))
        joint_c = Servo(webots_servo=self.WebotsController.addServo("Need Names Here"))
        joint_d = Servo(webots_servo=self.WebotsController.addServo("Need Names Here"))
        joint_e = Servo(webots_servo=self.WebotsController.addServo("Need Names Here"))
        self.Joints = [joint_a, joint_b, joint_c, joint_d, joint_e]

    def moveToPoint(self, x, y, z):
        joint_angles = self.manipulator.InchwormIK(x, y, z, self.a, self.b, self.c, self.d, self.e)
        # We can either stick this directly into webots, and it will go here based off the max speed the motors can go,
        # OR we make actual trajeectory planning

