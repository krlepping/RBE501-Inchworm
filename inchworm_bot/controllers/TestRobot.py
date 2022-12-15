import numpy as np

from MotorController import MotorController
from Manipulator import Manipulator
from math import pi
from time import sleep
Time_Step = 64

TARGETANGLESTATE = { # Old MATLAB WRONG numbers
    0:np.array([0,0,0,0,0]), # Zero
    # 1:np.array([0,0.54733525342,0.47612581994,0.54733525342,0]),
    1:np.array([0.5658,0.6371,0.0036,-0.2874,-0.4928]), # Y Reset
    # 2:np.array([101.997%(pi/2),-7.552%(pi/2),16.079%(pi/2), 39.751%(pi/2),732.369%(pi/2)]),
    2:np.array([0.1645,-0.4416,0.8482,0.1719,-0.2933]), # Y Line Pickup Box
    3:np.array([-1.1050,-1.6804,-8.5681,2.4030,-0.4075]), # X Reset
    4: np.array([-1.1050, -1.6804, -8.5681, 2.4030, -0.4075])  # X Line Pickup Box
}

TARGET = {
    0: np.array([[1,0,0,0],[0,1,0,169.9879],[0,0,1,0],[0,0,0,1]]),
    1: np.array([[0,0,-1,0],[0,1,0,150],[1,0,0,180],[0,0,0,1]]),
    2: np.array([[0,0,-1,0],[0,1,0,300],[1,0,0,50.8],[0,0,0,1]]),
    3: np.array([[1,0,0,150],[0,1,0,0],[0,0,1,180],[0,0,0,1]]),
    4: np.array([[0, -1, 0, 300], [0, 0, -1, 0], [1, 0, 0, 50.8], [0, 0, 0, 1]])
}

def main():
    print("Starting Inchworm Running")
    motorController = MotorController()
    man = Manipulator()
    np.set_printoptions(precision=3,suppress=True)
    i = 0
    j = 1
    targetT = TARGET.get(i, np.array([[1,0,0,0],[0,1,0,169.9879],[0,0,1,0],[0,0,0,1]]))
    print(f"Target {targetT}")
    targetQ = man.InchwormIK(targetT, np.array([0, 0, 0, 0, 0]))
    prevQ = np.array([0, 0, 0, 0, 0])
    differenceQ = targetQ - prevQ
    if isinstance(differenceQ, np.ndarray) and len(differenceQ.shape) >= 2:
        differenceQ = differenceQ[0]
    print(differenceQ)
    while motorController.robot.step(Time_Step) != -1:
        trajPoint = prevQ + differenceQ/100*j
        j+=1
        motorController.move(trajPoint)
        if j == 100:
            print(f"At {man.InchwormFK(trajPoint)}")
            i += 1
            j = 0
            prevQ = motorController.getJoints()
            targetT = TARGET.get(i, np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 169.9879], [0, 0, 0, 1]]))
            targetQ = man.InchwormIK(targetT,prevQ)
            differenceQ = targetQ - prevQ
            print(differenceQ)
            if isinstance(differenceQ, np.ndarray) and len(differenceQ.shape) >= 2:
                differenceQ = differenceQ[0]

        # difference = TARGETANGLESTATE.get(i, np.array([0, 0, 0, 0, 0])) - TARGETANGLESTATE.get(i - 1, np.array([0, 0, 0, 0, 0]))
        # Joints = TARGETANGLESTATE.get(i, np.array([0, 0, 0, 0, 0]))
        # trajPoint = TARGETANGLESTATE.get(i - 1, np.array([0, 0, 0, 0, 0]))+(difference/100*j)
        # motorController.move(trajPoint)
        # if np.linalg.norm(motorController.getJoints()-Joints) < 0.001:
        #     print(f"At {Joints}")
        #     i+=1
        #     print(i)
        #     j = 0
        #     previousJ = TARGET.get(i-1,np.array([[1,0,0,0],[0,1,0,163],[0,0,1,0],[0,0,0,1]]))



        # Joints = [0, 0, pi, 0, 0]
        # J = [0, 0, 0, 0, 0]
        # T = man.InchwormFK(Joints)
        # q = man.InchwormIK(T, J)
        # print(f"In position {T}")
        # print(f"Given {Joints}")
        # print(f"Found {q}")
