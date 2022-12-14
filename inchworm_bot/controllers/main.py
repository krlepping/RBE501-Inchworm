# from MotorController import MotorController
from Manipulator import Manipulator
from math import pi

Time_Step = 64

def main():
    print("Starting Inchworm Running")
    # motorController = MotorController()
    man = Manipulator()
    for i in range(1,100):
        Joints = [i*2*pi/100, 0, 0, 0, 0]
        J = [0,0,0,0,0]
        T = man.InchwormFK(Joints)
        q = man.InchwormIK(T,J) % (pi*2)
        print(f"Given {Joints}")
        print(f"Found {q}")



if __name__ == "__main__":
    main()