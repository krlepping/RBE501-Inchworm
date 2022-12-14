import numpy as np

from MotorController import MotorController
from Manipulator import Manipulator
from math import pi
from time import sleep
Time_Step = 64

STATE = {
    0:np.array([0,0,0,0,0]), # Zero
    1:np.array([0.5658,0.6371,0.0036,-0.2874,-0.4928]), # Y Reset
    2:np.array([0.1645,-0.4416,0.8482,0.1719,-0.2933]), # Y Line Pickup Box
    3:np.array([-1.1050,-1.6804,-8.5681,2.4030,-0.4075]), # X Reset
    4: np.array([-1.1050, -1.6804, -8.5681, 2.4030, -0.4075])  # X Line Pickup Box
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
    j = 1
    difference = STATE.get(i,np.array([0,0,0,0,0])) - STATE.get(i-1,np.array([0,0,0,0,0]))
    while motorController.robot.step(Time_Step) != -1:
        J = [0, 0, 0, 0, 0]
        j += 1
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        difference = STATE.get(i, np.array([0, 0, 0, 0, 0])) - STATE.get(i - 1, np.array([0, 0, 0, 0, 0]))
        Joints = STATE.get(i, np.array([0, 0, 0, 0, 0]))
        trajPoint = STATE.get(i - 1, np.array([0, 0, 0, 0, 0]))+(difference/100*j)
        print(trajPoint)
        motorController.move(trajPoint)
        if np.linalg.norm(motorController.getJoints()-Joints) < 0.001:
            print(f"At {Joints}")
            i+=1
            print(i)
            j = 0
            previousJ = STATE.get(i-1,np.array([0,0,0,0,0]))




        # Joints = [0, 0, pi, 0, 0]
        # J = [0, 0, 0, 0, 0]
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        # print(f"In position {T}")
        # print(f"Given {Joints}")
        # print(f"Found {q}")
