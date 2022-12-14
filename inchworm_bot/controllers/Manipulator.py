"""
Author: Chandler Garcia
This manipulator class was created based off of what we were learning in class,
Was originally going to write it all in python, but I learned that you can actually use matlab in python so that's
just what I'll do instead
"""

import math as math
import numpy as np

class Manipulator:
    def __init__(self):
        # Hopefully I can just get it working
        self.footHeight1 = 38.40
        self.AnkleHeight1 = 109.03
        self.AnkleHeight2 = 109.03 # Real value seems to be different, oop
        self.legLength1 = 163.32
        self.defaultAngle = 58.64 * math.pi / 180


        self.M = np.array([[1,0,0,self.legLength1*math.cos(self.defaultAngle)*2],
                           [0,1,0,0],
                           [0,0,1,0],
                           [0,0,0,1]])
        self.S = np.array([[0, 0, 1, 0, 0, 0],
                           [0, 1, 0, -self.AnkleHeight1, 0, 0],
                           [0, 1, 0, -self.AnkleHeight1 - self.legLength1 * math.sin(self.defaultAngle),
                            0, self.legLength1 * math.sin(self.defaultAngle)],
                           [0, 1, 0, -self.AnkleHeight2, 0, self.legLength1 * math.sin(self.defaultAngle) * 2],
                           [0, 0, 1, 0, 0, self.legLength1 * math.sin(self.defaultAngle) * 2]])

    def InchwormFK(self, q):
        """
        Takes in all 5 joint angles and returns the foot position, Joints is a [] of Servos currently
        :param Joints: The joints of the robot, in order
        :return:
        """

        return RodriguesFormula(self.S,self.M,q)

    def InchwormIK(self,x,y,z,alpha,beta,gamma):
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
        # IK = self.eng.IK_Inchworm(x,y,z,a,b,c,d,e,alpha,beta,gamma)
        # TODO: Make this work
        # return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure

    def InchwormIK(self,x,y,z):
        """
        Go to point, final orientation doesn't matter
        xyz coordinates we want to go
        :param x:
        :param y:
        :param z:

        Initial position of the arm (current Q)
        :param Joints: The joints of the robot, in order
        """
        # IK = self.eng.IK_InchwormNoOrientation(x,y,z,a,b,c,d,e)
        # TODO: Make this work, and parse the return IK for proper info
        # return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure

    def InchwormIK(self,T,joints):
        """
        Go to point, final orientation doesn't matter
        xyz coordinates we want to go
        :param T: where and how to face when acheiving wanted position
        :param joints: Initial joint angles

        Initial position of the arm (current Q)
        :param Joints: The joints of the robot, in order
        """

        return newton_raphson(T,joints,0.0001,1000,self.S,self.M)
        # TODO: Make this work, and parse the return IK for proper info
        # return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure


def newton_raphson(targetT,initialJointAngles,epsilon,max_iter,S,M):
    currentQ = initialJointAngles
    currentT = RodriguesFormula(S,M,initialJointAngles)
    currentPose = currentT[0:3,3]
    targetPose = targetT[0:3,3]
    lamb = 0.5
    iteration = 0
    while np.linalg.norm(targetT - currentT) > epsilon and iteration <= max_iter:
        J_a = jacoba(S,M,currentQ) # Need to put it into column form, is currently in row form
        # J = jacob0(S,currentQ) # Need to put it into column form, is currently in row form
        error = (targetPose - currentPose)
        # poseError = lamb**2 * np.eye(3) @ error
        # JaJaInv = J_a @ J_a.conj().T
        # deltaQ = J_a @ np.linalg.pinv(JaJaInv + poseError)
        pinv = np.linalg.pinv(J_a)
        deltaQ = (pinv @ error)
        currentQ = currentQ + deltaQ.conj().T
        currentT = RodriguesFormula(S,M,currentQ)
        currentPose = currentT[0:3, 3]
        iteration+=1
    return currentQ




def RodriguesFormula(S,M,jointAngles):
    T = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    for i in range(0,len(jointAngles)-1):
        T = T @ twist2ht(S[i],jointAngles[i])
    T = T@M
    return T

def jacoba(S,M,q):
    J_space = jacob0(S,q).conj().T
    Jws = J_space[0:3,:]
    Jvs = J_space[3:6,:]
    T = RodriguesFormula(S,M,q)
    p = T[0:3,3]
    ret = -skew(p) @ Jws + Jvs
    return ret

def jacob0(S,q):
    T = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    for i in range(0,len(q)):
        temp = twist2ht(S[i],q[i])
        T = T @ temp
        if i != 0:
            adj = adjoint(S[i],T)
            J = np.vstack((J,adj))
        else:
            J = [S[i]]
    return J

def adjoint(Va,T):
    R = T[0:3,0:3]
    P = T[3,0:3]
    right = np.zeros((3,3))
    dom = np.hstack((R,right))
    sub = np.hstack((skew(P)@R,R))
    Adj = np.vstack((dom,sub))
    return Adj @ Va

def twist2ht(S,angle):
    R = axisAngle2Rot(S[0:3],angle)
    part1 = np.eye(3) * angle
    part2 = (1 - math.cos(angle)) * skew(S[0:3])
    part3 = (angle - math.sin(angle)) * (skew(S[0:3]) @ skew(S[0:3]))
    shite = (np.add(np.add(part1, part2), part3) @ S[3:6])
    top = np.hstack((R,shite.reshape(-1,1)))
    bottom = np.array([0,0,0,1])
    return np.vstack((top,bottom))

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
