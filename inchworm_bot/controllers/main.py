# from MotorController import MotorController
import numpy as np

from Manipulator import Manipulator
from math import pi

Time_Step = 64

def main():
    print("Starting Inchworm Running")
    # motorController = MotorController()
    np.set_printoptions(precision=3,suppress=True)
    man = Manipulator()
    Joints = [0,0.54733525342,0.47612581994,0.54733525342,0]
    J = [0,0,0,0,0]

    print(f"Test {man.JacobA(Joints)}")

    T = man.InchwormFK(Joints)
    q = man.InchwormIK(T,J)

    print(f"In position \n{T}")
    print(f"Given {Joints}")
    print(f"Found {q}")



if __name__ == "__main__":
    main()