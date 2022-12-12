from controller import Robot, Motor

TIME_STEP = 64

# create the Robot instance.
#use this to test moving the different motors
robot = Robot()

# get the motor devices
foot2Motor = robot.getDevice('foot_ankle_motor2')
foot1Motor = robot.getDevice('foot_ankle_motor1')
centerMotor = robot.getDevice('center_motor')
ankle1Motor = robot.getDevice('ankle_leg_motor1')
ankle2Motor = robot.getDevice('ankle_leg_motor2')


# set the target position of the motors
#foot1Motor.setPosition(0.0)
#foot2Motor.setPosition(0.0)
#centerMotor.setPosition(0.0)
#ankle1Motor.setPosition(0.0)
#ankle2Motor.setPosition(0.0)

foot1Motor.setPosition(1.0)
foot2Motor.setPosition(1.0)
centerMotor.setPosition(1.0)
ankle1Motor.setPosition(1.0)
ankle2Motor.setPosition(1.0)

foot1Motor.getTargetPosition()
foot2Motor.getTargetPosition()
centerMotor.getTargetPosition()
ankle1Motor.getTargetPosition()
ankle2Motor.getTargetPosition()





while robot.step(TIME_STEP) != -1:
   pass
