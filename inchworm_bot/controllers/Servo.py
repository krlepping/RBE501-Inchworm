from math import radians

"""
This class is using Dan Moyer's code base to initialize and keep change information
"""


class Servo:
    def __init__(self, webots_servo=None):
        self.webots_servo = webots_servo
        self.angle = 0

    def setAngle(self, angle):
        self.angle = angle
        if self.physical_servo is not None:
            self.physical_servo.angle = max(0, min(180, angle + self.offset))
        if self.webots_servo is not None:
            self.webots_servo.setPosition(radians(angle))
