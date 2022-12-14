from MotorController import MotorController
from Manipulator import Manipulator
from math import pi
Time_Step = 2

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
        Joints = [i * 2 * pi / 100, 0, 0, 0, 0]
        J = [0, 0, 0, 0, 0]
        T = man.InchwormFK(Joints)
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
