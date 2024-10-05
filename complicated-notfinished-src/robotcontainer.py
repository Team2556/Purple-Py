# Create the robot container class

import wpilib
from wpilib import SmartDashboard
from commands2 import CommandScheduler
from subsystems.drivetrain import SwerveDrivetrain
from subsystems.limelight import Limelight
from subsystems.navx import NavX
# from commands import SwerveDrive

class RobotContainer:
    def __init__(self):
        # Create all of your subsystems
        self.swerveDrivetrain = SwerveDrivetrain()
        self.limelight = Limelight()
        self.navx = NavX()
        # Configure the button bindings
        self.configureButtonBindings()
        # Set the default commands
        self.setDefaultCommands()

    def configureButtonBindings(self):
        pass

    def setDefaultCommands(self):
        # Set the default commands for a subsystem here.
        # Example:
        # self.swerveDrivetrain.setDefaultCommand(SwerveDrive(self.swerveDrivetrain))
        pass

    def autonomousInit(self):
        # Schedule the autonomous command
        pass

    def autonomousPeriodic(self):
        # Runs the Scheduler.  This is where the robot's subsystems are scheduled.
        CommandScheduler.getInstance().run()

    def teleopInit(self):
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        CommandScheduler.getInstance().cancelAll()

    def teleopPeriodic(self):
        # Runs the Scheduler.  This is where the robot's subsystems are scheduled.
        CommandScheduler.getInstance().run()

    def testInit(self):
        # Cancels all running commands at the start of test mode.
        CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self):
        # Runs the Scheduler.  This is where the robot's subsystems are scheduled.
        CommandScheduler.getInstance().run()

    def disabledInit(self):
        # Runs the Scheduler.  This is where the robot's subsystems are scheduled.
        CommandScheduler.getInstance().run()

    def disabledPeriodic(self):
        # Runs the Scheduler.  This is where the robot's subsystems are scheduled.
        CommandScheduler.getInstance().run()