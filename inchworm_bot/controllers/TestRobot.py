from MotorController import MotorController
from Manipulator import Manipulator
from math import pi
Time_Step = 2

def main():
    print("Starting Inchworm Running")
    motorController = MotorController()
    # man = Manipulator()
    # Joints = [0,0,0,0,0]
    # man.InchwormFKNoWebots(Joints)
    # motorController.whereAt()
    i = 0
    while motorController.robot.step(Time_Step) != -1:
        motorController.move(pi/100*i)
        motorController.whereAt()

        i+=1
        print(i)
