import wpilib
from commands2 import CommandScheduler, Subsystem
# from wpimath.kinematics import 
from phoenix5 import WPI_TalonSRX, WPI_TalonFX, TalonSRX

from constants import DriveConstant
from wpilib import SmartDashboard
import wpilib.shuffleboard as shuffleboard



class Drivetrain(Subsystem):
    def __init__(self):
        super().__init__()
        CommandScheduler.registerSubsystem(self)
        shuffleboard.DrivetrainTab = shuffleboard.Shuffleboard.getTab("Drivetrain")
        shuffleboard.DrivetrainTab.add("Drivetrain", self)

        # super().__init__()
        # define the 4 drive motors
        self.mtrDrive_frontLeft = WPI_TalonFX(DriveConstant.kLeftMotorFront_DrivePort)
        self.mtrDrive_frontRight = WPI_TalonFX(DriveConstant.kRightMotorFront_DrivePort)
        self.mtrDrive_backLeft = WPI_TalonFX(DriveConstant.kLeftMotorRear_DrivePort)
        self.mtrDrive_backRight = WPI_TalonFX(DriveConstant.kRightMotorRear_DrivePort)

        # define the 4 drive encoders
        self.encDrive_frontLeft = self.mtrDrive_frontLeft
        self.encDrive_frontRight = self.mtrDrive_frontRight
        self.encDrive_backLeft = self.mtrDrive_backLeft
        self.encDrive_backRight = self.mtrDrive_backRight

        #define the 4 steer motors
        self.mtr_Steer_frontLeft = TalonSRX(DriveConstant.kLeftMotorFront_SteerPort)
        self.mtr_Steer_frontRight = TalonSRX(DriveConstant.kRightMotorFront_SteerPort)
        self.mtr_Steer_backLeft = TalonSRX(DriveConstant.kLeftMotorRear_SteerPort)
        self.mtr_Steer_backRight = TalonSRX(DriveConstant.kRightMotorRear_SteerPort)

        # define the 4 steer encoders
        self.enc_Steer_frontLeft = self.mtr_Steer_frontLeft
        self.enc_Steer_frontRight = self.mtr_Steer_frontRight
        self.enc_Steer_backLeft = self.mtr_Steer_backLeft
        self.enc_Steer_backRight = self.mtr_Steer_backRight

        shuffleboard.DrivetrainTab.add("Front Left Drive", SmartDashboard(self.mtrDrive_frontLeft))
        shuffleboard.DrivetrainTab.add("Front Right Drive", self.mtrDrive_frontRight)
        shuffleboard.DrivetrainTab.add("Back Left Drive", self.mtrDrive_backLeft)
        shuffleboard.DrivetrainTab.add("Back Right Drive", self.mtrDrive_backRight)
        shuffleboard.DrivetrainTab.add("Front Left Steer", self.mtr_Steer_frontLeft)
        shuffleboard.DrivetrainTab.add("Front Right Steer", self.mtr_Steer_frontRight)
        shuffleboard.DrivetrainTab.add("Back Left Steer", self.mtr_Steer_backLeft)
        shuffleboard.DrivetrainTab.add("Back Right Steer", self.mtr_Steer_backRight)



        
