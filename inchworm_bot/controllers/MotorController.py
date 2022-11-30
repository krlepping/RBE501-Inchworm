import Manipulator
import math as math
from WebotsServoController import WebotsServoController
from Servo import Servo

class MotorController:
    def __init__(self):
        self.manipulator = Manipulator
        self.WebotsController = WebotsServoController()

        joint_a = Servo(webots_servo=self.WebotsController.addServo("foot_ankle_joint2"))
        joint_b = Servo(webots_servo=self.WebotsController.addServo("ankle_leg_joint2"))
        joint_c = Servo(webots_servo=self.WebotsController.addServo("center_joint"))
        joint_d = Servo(webots_servo=self.WebotsController.addServo("leg_ankle_joint1"))
        joint_e = Servo(webots_servo=self.WebotsController.addServo("ankle_foot_joint1"))
        self.Joints = [joint_a, joint_b, joint_c, joint_d, joint_e]

    def moveToPoint(self, x, y, z):
        joint_angles = self.manipulator.InchwormIK(x, y, z, self.Joints)
        # We can either stick this directly into webots, and it will go here based off the max speed the motors can go,
        # OR we make actual trajeectory planning

