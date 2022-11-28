"""
Author: Chandler Garcia
This manipulator class was created based off of what we were learning in class, and follows a similar format to the
sQuadruped Manipulator.py that Dan Moyer made for my legged robotics project.
I am only documenting this because my memory is horrible and I will probably re-use this code in the future.
"""

import math as math
import numpy as np
import matlab.engine


class Manipulator:
    default_S = [0, 0, 1, 0, 0, 0]
    default_M = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1] # Setup as a 1D arraw so its easier to parse long term

    def __init__(self):
        self.S = [] # Skew symmetric
        self.M = [] # Frame, 1D array 0 through
        self.Mtrans = [] # Transitioins from each joint (M12, M23, etc), 2D array following M's format
        self.eng = matlab.engine.start_matlab() # Makes my life so much easier, no need to create new FK and IK scripts

    def addRevoluteJoint(self, w, p, BaseFrame = default_M):
        """
        Add a joint to the existing robot, joint gets added to the previous joint added
        :param w: Way the joint is pointing
        :param p: Where the robot is in respect to the starting point, could be initial joint or connection with ground
        :param BaseFrame: The base frame of the robot, initially 0 0 0 0 0 0 xyzabc
        :return:
        """
        Mprev = self.M # Using this for finding Mtrans
        self.M[3] = p[0] + BaseFrame[3]
        self.M[7] = p[1] + BaseFrame[7]
        self.M[11] = p[2] + BaseFrame[11]
        S = w + list(np.cross(p, w))

        self.Mtrans.append(np.add(-Mprev,self.M))
        # This is assuming that each joint fram change is in respect to the initial fram
        self.S.append(S)


    def addPrismaticJoint(self, w, p, M = default_M):
        """
        This should not be used, as the inchworm has no prismatic joints, but it is here because I want to reuse this
        class for future projects
        This function will be empty until I feel like I should fill it
        :param s:
        :param w:
        :return:
        """

    def twist2ht(self, S, theta):
        """
        Helper function for IK and FK
        :param S:
        :param theta:
        :return:
        """
        R = self.axisangle2rot(S[1:3],theta)


    def axisangle2rot(self, omega, theta):
        """
        Helper function for twist2ht
        :param omega:
        :param theta:
        :return:
        """
        omega_ss = np.array([[0, -omega[2], omega[1]], [omega[2], 0, -omega[0]], [-omega[1], omega[0], 0]])
        return np.identity(3) + math.sin(theta) * omega_ss + (1- math.cos(theta)) * np.multiply(omega_ss,omega_ss)
