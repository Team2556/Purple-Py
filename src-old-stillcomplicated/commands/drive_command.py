from commands2 import Command
from phoenix5 import WPI_TalonFX, WPI_TalonSRX
from subsystems.drivetrain import Drivetrain
from phoenix5 import WPI_TalonSRX, WPI_TalonFX, ControlMode


class AlignCommands(Command):
    def __init__(self, drivetrain: Drivetrain):
        super().__init__()#drivetrain)
        self.drivetrain = drivetrain
        self.addRequirements(drivetrain)
        # self.mtrDrive_frontLeft = self.drivetrain.mtrDrive_frontLeft
        # self.mtrDrive_frontRight = self.drivetrain.mtrDrive_frontRight
        # self.mtrDrive_backLeft = self.drivetrain.mtrDrive_backLeft
        # self.mtrDrive_backRight = self.drivetrain.mtrDrive_backRight
        # self.encDrive_frontLeft = self.drivetrain.encDrive_frontLeft
        # self.encDrive_frontRight = self.drivetrain.encDrive_frontRight
        # self.encDrive_backLeft = self.drivetrain.encDrive_backLeft
        # self.encDrive_backRight = self.drivetrain.encDrive_backRight
        # self.mtr_Steer_frontLeft = self.drivetrain.mtr_Steer_frontLeft
        self.mtr_Steer_frontRight = self.drivetrain.mtr_Steer_frontRight
        # self.mtr_Steer_backLeft = self.drivetrain.mtr_Steer_backLeft
        # self.mtr_Steer_backRight = self.drivetrain.mtr_Steer_backRight
        # self.enc_Steer_frontLeft = self.drivetrain.enc_Steer_frontLeft
        # self.enc_Steer_frontRight = self.drivetrain.enc_Steer_frontRight
        # self.enc_Steer_backLeft = self.drivetrain.enc_Steer_backLeft
        # self.enc_Steer_backRight = self.drivetrain.enc_Steer_backRight

        def align_steer_module(self, target:WPI_TalonSRX, angle:float=0):
            target.set(ControlMode.Position, angle)
        def execute(self):
            self.align_steer_module(target=self.mtr_Steer_frontRight, angle=0)

    # def execute(self, target:WPI_TalonSRX, angle:float):
    #     target.set(ControlMode.Position, angle)


