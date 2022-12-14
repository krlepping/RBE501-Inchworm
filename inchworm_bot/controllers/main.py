# from MotorController import MotorController
import numpy as np

from Manipulator import Manipulator
from math import pi

Time_Step = 64

def main():
    print("Starting Inchworm Running")
    # motorController = MotorController()
    man = Manipulator()
    Joints = [0, -31.36*pi/180, 0, 0, 0]
    J = [0,0,0,0,0]
    T = man.InchwormFK(Joints)
    q = man.InchwormIK(T,J)
    np.set_printoptions(precision=3,suppress=True)
    print(f"In position \n{T}")
    print(f"Given {Joints}")
    print(f"Found {q}")



if __name__ == "__main__":
    main()