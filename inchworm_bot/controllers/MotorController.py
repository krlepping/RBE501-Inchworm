import Manipulator
import math as math
class MotorController:
    def __init__(self):
        """
        each motor has a current start position and a max and min that they can turn
        The order goes
        Min, Max, Start Position
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

    def moveToPoint(self, x, y, z):
        self.manipulator.InchwormIK(x, y, z, self.a, self.b, self.c, self.d, self.e)



