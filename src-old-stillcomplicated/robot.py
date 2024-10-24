#boilerplate robotpy commandbased robot.py
import wpilib
from commands2 import TimedCommandRobot, CommandScheduler
from robotcontainer import RobotContainer
class MyRobot(TimedCommandRobot):
    def robotInit(self):
        # Initialization code here
        super().__init__()
        self.robotcontainer = RobotContainer()
        CommandScheduler.getInstance().run()

        pass

    def autonomousInit(self):
        # Code to run once when autonomous starts
        pass

    def autonomousPeriodic(self):
        # Code to run periodically during autonomous
        pass

    def teleopInit(self):
        # Code to run once when teleop starts
        pass

    def teleopPeriodic(self):
        # Code to run periodically during teleop
        pass

    def testPeriodic(self):
        # Code to run periodically during test mode
        pass



