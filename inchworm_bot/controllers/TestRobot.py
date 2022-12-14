import numpy as np

from MotorController import MotorController
from Manipulator import Manipulator
from math import pi
from time import sleep
Time_Step = 64

STATE = {
    0:np.array([0.5658,0.6371,0.0036,-0.2874,-0.4928]), # Y Reset
    1:np.array([-0.0824,0.0095,0.4229,0.2191,0.1457]) # Y Line Pickup Box

}

def main():
    print("Starting Inchworm Running")
    motorController = MotorController()
    man = Manipulator()
    # man = Manipulator()
    # Joints = [0,0,0,0,0]
    # man.InchwormFKNoWebots(Joints)
    # motorController.whereAt()
    i = 0
    while motorController.robot.step(Time_Step) != -1:
        J = [0, 0, 0, 0, 0]
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        Joints = STATE.get(i, np.array([0, 0, 0, 0, 0]))
        motorController.move(Joints)
        if np.linalg.norm(motorController.getJoints()-Joints) < 0.001:
            print(f"At {Joints}")
            i+=1
            print(i)




        # Joints = [0, 0, pi, 0, 0]
        # J = [0, 0, 0, 0, 0]
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        # print(f"In position {T}")
        # print(f"Given {Joints}")
        # print(f"Found {q}")
