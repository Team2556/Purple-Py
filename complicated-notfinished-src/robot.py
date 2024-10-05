# Use Robotpy to drive the robot
# robot will have a swerve drivebase
# each swerve module will have a kracken drive motor Neo 550 steering motors
# robot will have a limelight vision sensor for apriltag based localization
# robot will have a navx for gyro based localization

import wpilib
from wpilib import SmartDashboard
from commands2 import TimedCommandRobot
from robotcontainer import RobotContainer


# putting in the typical command based robot class; most of the code will be in robotcontainer, subsystems, and commands
class MyRobot(TimedCommandRobot):
    def robotInit(self):
        self.robotContainer = RobotContainer()

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        self.robotContainer.autonomousInit()

    def autonomousPeriodic(self):
        self.robotContainer.autonomousPeriodic()

    def teleopInit(self):
        self.robotContainer.teleopInit()

    def teleopPeriodic(self):
        self.robotContainer.teleopPeriodic()

    def testInit(self):
        self.robotContainer.testInit()

    def testPeriodic(self):
        self.robotContainer.testPeriodic()

    def disabledInit(self):
        self.robotContainer.disabledInit()

    def disabledPeriodic(self):
        self.robotContainer.disabledPeriodic()