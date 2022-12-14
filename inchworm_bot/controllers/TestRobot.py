import numpy as np

from MotorController import MotorController
from Manipulator import Manipulator
from math import pi
Time_Step = 16

def main():
    print("Starting Inchworm Running")
    motorController = MotorController()
    man = Manipulator()
    Joints = [0.1789,0.2135,-0.1146,-0.1252,-0.1576]
    # man = Manipulator()
    # Joints = [0,0,0,0,0]
    # man.InchwormFKNoWebots(Joints)
    # motorController.whereAt()
    i = 0
    while motorController.robot.step(Time_Step) != -1:
        J = [0, 0, 0, 0, 0]
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        motorController.move(Joints)
        print(f"Given {Joints}")
        print(f"Found {Joints}")
        i+=1
        print(i)

        # Joints = [0, 0, pi, 0, 0]
        # J = [0, 0, 0, 0, 0]
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        # print(f"In position {T}")
        # print(f"Given {Joints}")
        # print(f"Found {q}")
