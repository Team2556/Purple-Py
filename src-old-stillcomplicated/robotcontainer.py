import commands2
import wpilib
from commands2.button import CommandXboxController as XboxController
from commands2 import CommandScheduler

from subsystems.drivetrain import Drivetrain
from commands.drive_command import AlignCommands
from constants import DriveConstant, OIConstant

class RobotContainer:
    def __init__(self):
        # Initialize the subsystems
        self.drivetrain = Drivetrain()

        # Initialize the controller
        self.driver_controller = XboxController(OIConstant.kDriver1ControllerPort)

        self.AllignCommands = AlignCommands(self.drivetrain)

        # Configure the button bindings
        self.configure_button_bindings()


        # Set the default command for the drivetrain
        # self.drivetrain.setDefaultCommand(
        #     DriveCommand(
        #         self.drivetrain,
        #         lambda: self.driver_controller.getLeftY(),
        #         lambda: self.driver_controller.getRightX()
        #     )
        # )

    def configure_button_bindings(self):
        # Example of button binding
        # self.driver_controller.getAButton().whenPressed(SomeCommand(self.drivetrain))
        # fn_align_steer_module = AlignCommands.align_steer_module_front_right(target = self.drivetrain.mtr_Steer_frontRight, angle = 0)
        self.driver_controller.a().onTrue(self.AllignCommands)
        

    def get_autonomous_command(self):
        # Return the command to run in autonomous
        return None
