"""
Author: Chandler Garcia
This manipulator class was created based off of what we were learning in class,
Was originally going to write it all in python, but I learned that you can actually use matlab in python so that's
just what I'll do instead
"""

import math as math
import numpy as np
import matlab.engine


class Manipulator:
    # default_S = [0, 0, 1, 0, 0, 0]
    # default_M = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1] # Setup as a 1D arraw so its easier to parse long term

    def __init__(self):
        # self.S = [] # Skew symmetric
        # self.M = [] # Frame, 1D array 0 through
        # self.Mtrans = [] # Transitioins from each joint (M12, M23, etc), 2D array following M's format
        self.eng = matlab.engine.start_matlab() # Makes my life so much easier, no need to create new FK and IK scripts
        self.eng.addpath(r'/home/midnightpegasus/Documents/WPI/RobotDynamics/Final_Project/RBE501-Inchworm/inchworm_bot/controllers',nargout=5)

    def InchwormFK(self, a, b, c, d, e):
        """
        Takes in all 5 joint angles and returns the foot position
        :param a:
        :param b:
        :param c:
        :param d:
        :param e:
        :return:
        """
        T = self.eng.FK_Inchworm(a,b,c,d,e)

    def InchwormIK(self,x,y,z,a,b,c,d,e,alpha,beta,gamma):
        """
        xyz coordinates we want to go
        :param x:
        :param y:
        :param z:

        Initial position of the arm (current Q)
        :param a:
        :param b:
        :param c:
        :param d:
        :param e:

        xyz Euler coordinates of final position we want
        :param alpha:
        :param beta:
        :param gamma:
        :return:
        """
        IK = self.eng.IK_Inchworm(x,y,z,a,b,c,d,e,alpha,beta,gamma)
        return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure

    def InchwormIK(self,x,y,z,a,b,c,d,e):
        """
        Go to point, final orientation doesn't matter
        xyz coordinates we want to go
        :param x:
        :param y:
        :param z:

        Initial position of the arm (current Q)
        :param a:
        :param b:
        :param c:
        :param d:
        :param e:
        """
        IK = self.eng.IK_InchwormNoOrientation(x,y,z,a,b,c,d,e)
        return IK # Might need to change this return type to be a list instead of what it might be - maybe a string, unsure
