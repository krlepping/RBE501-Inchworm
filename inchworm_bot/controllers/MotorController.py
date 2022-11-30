import Manipulator
import math as math
from WebotsServoController import WebotsServoController

class MotorController:
    def __init__(self):
        """
        each motor has a current start position and a max and min that they can turn
        The order goes
        Start Position
        Limiters
        """
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0

        self.motor1 = [-math.pi, math.pi]
        self.motor2 = [-math.pi, math.pi]
        self.motor3 = [-math.pi, math.pi]
        self.motor4 = [-math.pi, math.pi]
        self.motor5 = [-math.pi, math.pi]
        self.manipulator = Manipulator
        self.WebotsController = WebotsServoController()

    def moveToPoint(self, x, y, z):
        joint_angles = self.manipulator.InchwormIK(x, y, z, self.a, self.b, self.c, self.d, self.e)
        # We can either stick this directly into webots, and it will go here based off the max speed the motors can go,
        # OR we make actual trajeectory planning

