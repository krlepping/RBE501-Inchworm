from Manipulator import Manipulator
from WebotsServoController import WebotsServoController
from controller import Robot, Motor
from math import pi
from time import sleep



class MotorController:
    def __init__(self):
        print("Motor Controller Initializing")
        self.manipulator = Manipulator()
        print("Manipulator Initialized")
        # Create Robot Instance
        self.robot = WebotsServoController()
        print("Webots Controller Initializing")

        # get the motor devices
        self.joint_a = self.robot.addServo('foot_ankle_motor2')
        self.joint_e = self.robot.addServo('foot_ankle_motor1')
        self.joint_c = self.robot.addServo('center_motor')
        self.joint_d = self.robot.addServo('ankle_leg_motor1')
        self.joint_b = self.robot.addServo('ankle_leg_motor2')


    def whereAt(self):
        a = self.joint_a.getTargetPosition()
        b = self.joint_b.getTargetPosition()
        c = self.joint_c.getTargetPosition()
        d = self.joint_d.getTargetPosition()
        e = self.joint_e.getTargetPosition()
        print(f"Joint 1 {a}, Joint 2 {b}, Joint 3 {c}, Joint 4 {d}, Joint 5 {e}")
        q = [a, b, c, d, e]
        position = self.manipulator.InchwormFK(q)
        print(f"{position}")
        return position

    def move(self,angle):
        self.joint_a.setPosition(angle[0])
        self.joint_b.setPosition(angle[1])
        self.joint_c.setPosition(angle[2])
        self.joint_d.setPosition(angle[3])
        self.joint_e.setPosition(angle[4])



    def moveToPoint(self, x, y, z):
        joint_angles = self.manipulator.InchwormIK(x, y, z, self.Joints)
        print(f"{joint_angles}")
        return joint_angles
        


