# import MotorController
from Manipulator import Manipulator

def main():
    man = Manipulator()
    Joints = [0,0,0,0,0]
    man.InchwormFKNoWebots(Joints)
    # motorController.whereAt()

if __name__ == "__main__":
    main()