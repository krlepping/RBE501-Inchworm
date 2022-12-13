from MotorController import MotorController
from Manipulator import Manipulator

def main():
    print("Starting Inchworm Running")
    motorController = MotorController()
    # man = Manipulator()
    # Joints = [0,0,0,0,0]
    # man.InchwormFKNoWebots(Joints)
    # motorController.whereAt()
    while True:
        motorController.whereAt()

if __name__ == "__main__":
    main()