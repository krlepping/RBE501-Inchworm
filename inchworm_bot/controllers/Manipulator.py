"""
Author: Chandler Garcia
This manipulator class was created based off of what we were learning in class,
Was originally going to write it all in python, but I learned that you can actually use matlab in python so that's
just what I'll do instead
"""

import math as math
import numpy as np
# import matlab.engine
from scipy.spatial.transform import Rotation as R

class Manipulator:
    def __init__(self):
        # self.eng = matlab.engine.start_matlab() # Makes my life so much easier, no need to create new FK and IK scripts
        # self.eng.addpath(r'/home/midnightpegasus/Documents/WPI/RobotDynamics/Final_Project/RBE501-Inchworm/inchworm_bot/controllers')
        # Hopefully I can just get it working
        self.footHeight1 = 38.40
        self.AnkleHeight1 = 109.03
        self.AnkleHeight2 = 109.03 # Real value seems to be different, oop
        self.legLength1 = 163.71
        self.defaultAngle = 58.64 * math.pi / 180

        # self.eng.FK_Inchworm(nargout=1)
        self.M = np.array([[1,0,0,self.legLength1*math.cos(self.defaultAngle)*2],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
        self.S = np.array([[0, 0, 1, 0, 0, 0],
                           [0, 1, 0, self.AnkleHeight1, 0, 0],
                           [0, 1, 0, self.AnkleHeight1 + self.legLength1 * math.sin(self.defaultAngle),
                            -self.legLength1 * math.sin(self.defaultAngle), 0],
                           [0, 1, 0, self.AnkleHeight2, -self.legLength1 * math.sin(self.defaultAngle) * 2, 0],
                           [0, 1, 0, 0, -self.legLength1 * math.sin(self.defaultAngle) * 2, 0]])
        # print(self.eng.test())

    def InchwormFK(self, Joints):
        """
        Takes in all 5 joint angles and returns the foot position, Joints is a [] of Servos currently
        :param Joints: The joints of the robot, in order
        :return:
        """
        a = Joints[0].getPosition()
        b = Joints[1].getPosition()
        c = Joints[2].getPosition()
        d = Joints[3].getPosition()
        e = Joints[4].getPosition()
        print(f"Joint 1 {a}, Joint 2 {b}, Joint 3 {c}, Joint 4 {d}, Joint 5 {e}")
        # T = self.eng.FK_Inchworm(a,b,c,d,e)

    def InchwormFKNoWebots(self, Joints):
        """
        Takes in all 5 joint angles and returns the foot position, Joints is a [] of Servos currently
        :param Joints: The joints of the robot, in order
        :return:
        """
        a = Joints[0]
        b = Joints[1]
        c = Joints[2]
        d = Joints[3]
        e = Joints[4]
        print(f"Joint 1 {a}, Joint 2 {b}, Joint 3 {c}, Joint 4 {d}, Joint 5 {e}")
        # T = self.eng.FK_Inchworm(0.0,0.0,0.0,0.0,0.0)
        RodriguesFormula(self.S,self.M,Joints)

    def InchwormIK(self,x,y,z,Joints,alpha,beta,gamma):
        """
        xyz coordinates we want to go
        :param x:
        :param y:
        :param z:

        Initial position of the arm (current Q)
        :param Joints: The joints of the robot, in order

        xyz Euler coordinates of final position we want
        :param alpha:
        :param beta:
        :param gamma:
        :return:
        """
        a = Joints[0].getPosition()
        b = Joints[1].getPosition()
        c = Joints[2].getPosition()
        d = Joints[3].getPosition()
        e = Joints[4].getPosition()
        # IK = self.eng.IK_Inchworm(x,y,z,a,b,c,d,e,alpha,beta,gamma)
        # TODO: Make this work
        # return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure

    def InchwormIK(self,x,y,z,Joints):
        """
        Go to point, final orientation doesn't matter
        xyz coordinates we want to go
        :param x:
        :param y:
        :param z:

        Initial position of the arm (current Q)
        :param Joints: The joints of the robot, in order
        """
        a = Joints[0].getPosition()
        b = Joints[1].getPosition()
        c = Joints[2].getPosition()
        d = Joints[3].getPosition()
        e = Joints[4].getPosition()
        # IK = self.eng.IK_InchwormNoOrientation(x,y,z,a,b,c,d,e)
        # TODO: Make this work, and parse the return IK for proper info
        # return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure


def newton_raphson(targetT,initialJointAngles,epsilon,max_iter,S,M):
    currentQ = initialJointAngles
    currentT = RodriguesFormula(S,M,initialJointAngles)
    while np.linalg.norm(targetT - currentT) > epsilon:



def RodriguesFormula(S,M,jointAngles):
    for i in range(0,len(jointAngles)-1):
        T = twist2ht(S[i],jointAngles[i])
    T = T@M
    print(T)
    return T

def jacoba(S,M,q):
    J_space = jacob0(S,q)
    Jws = J_space[0:3,:]
    Jvs = J_space[0:3, :]
    T = RodriguesFormula(S,M,q)
    p = T[0:3,3]

def jacob0(S,q):



def twist2ht(S,angle):
    R = axisAngle2Rot(S[0:3],angle)
    part1 = np.eye(3) * angle
    part2 = (1 - math.cos(angle)) * skew(S[0:3]).conj().T
    part3 = (angle - math.sin(angle)) * (skew(S[0:3]) @ skew(S[0:3])).conj().T
    shite = (np.add(np.add(part1, part2), part3) @ S[3:6])
    bottom = np.array([0,0,0,1])
    return np.vstack((np.hstack((R,shite.reshape(-1,1))),bottom))

def skew(S):
    if (isinstance(S, np.ndarray) and len(S.shape) >= 2):
        return np.array([[0, -S[2][0], S[1][0]],
                         [S[2][0], 0, -S[0][0]],
                         [-S[1][0], S[0][0], 0]])
    else:
        return np.array([[0, -S[2], S[1]],
                         [S[2], 0, -S[0]],
                         [-S[1], S[0], 0]])

def axisAngle2Rot(omega,theta):
    omega_ss = skew(omega)
    eye = np.eye(3)
    return np.add(np.add(eye,math.sin(theta) * omega_ss),(1- math.cos(theta)) * (omega_ss @ omega_ss))
