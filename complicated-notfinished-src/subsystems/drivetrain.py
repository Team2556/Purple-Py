
from commands2 import subsystem, SwerveControllerCommand
import wpilib
#import the libraries for robotpy swervedrive
from wpilib import SmartDashboard
from wpimath.geometry import Translation2d, Rotation2d
from wpimath.kinematics import (SwerveDrive4Kinematics, 
                                SwerveDrive4Odometry, 
                                SwerveModuleState, 
                                SwerveDrive4WheelPositions, 
                                SwerveModulePosition
                                # SwerveDrive4DriveDynamics
                                )
import phoenix6
from phoenix6.hardware import TalonFX#, TalonSRX 
from phoenix6.configs import TalonFXConfiguration
from phoenix5 import WPI_TalonSRX#, WPI_TalonFX
from rev import CANSparkLowLevel, CANSparkMax

import swervemodule
from constants import DriveConstant




class SwerveDrivetrain(subsystem):
    def __init__(self):#self, front_left, front_right, back_left, back_right):
        # define the module positions and a kinematics object
        halfBase = DriveConstant.kWheelBase/2
        halfWidth = DriveConstant.kTrackWidth/2
        self.frontLeftLocation = Translation2d(halfWidth, halfBase)
        self.frontRightLocation = Translation2d(halfWidth, -halfBase)
        self.backLeftLocation = Translation2d(-halfWidth, halfBase)
        self.backRightLocation = Translation2d(-halfWidth, -halfBase)
        self.kinematics = SwerveDrive4Kinematics(self.frontLeftLocation, self.frontRightLocation, self.backLeftLocation, self.backRightLocation)
        # define the drive motors for swerve drive
        self.frontLeft_drive = TalonFX(DriveConstant.kLeftMotorFront_DrivePort)
        self.frontRight_drive = TalonFX(DriveConstant.kRightMotorFront_DrivePort)
        self.backLeft_drive = TalonFX(DriveConstant.kLeftMotorRear_DrivePort)
        self.backRight_drive =  TalonFX(DriveConstant.kRightMotorRear_DrivePort)
        # define the steer motors for swerve drive
        neo550_cfg = CANSparkLowLevel.MotorType.kBrushless
        self.frontLeft_steer = CANSparkMax(DriveConstant.kLeftMotorFront_SteerPort, neo550_cfg)
        self.frontRight_steer = CANSparkMax(DriveConstant.kRightMotorFront_SteerPort, neo550_cfg)
        self.backLeft_steer = CANSparkMax(DriveConstant.kLeftMotorRear_SteerPort, neo550_cfg)
        self.backRight_steer = CANSparkMax(DriveConstant.kRightMotorRear_SteerPort, neo550_cfg)

        # define the encoders for the drive motors
        self.frontLeft_drive_enc = self.frontLeft_drive# .getEncoder()
        self.frontRight_drive_enc = self.frontRight_drive#.getEncoder()
        self.backLeft_drive_enc = self.backLeft_drive#.getEncoder()
        self.backRight_drive_enc = self.backRight_drive#.getEncoder()
        # define the encoders for the steer motors
        self.frontLeft_steer_enc = self.frontLeft_steer.getEncoder()
        self.frontRight_steer_enc = self.frontRight_steer.getEncoder()
        self.backLeft_steer_enc = self.backLeft_steer.getEncoder()
        self.backRight_steer_enc = self.backRight_steer.getEncoder()
        # define the PID controllers for the drive motors
        # talonfx_cfg = TalonFXConfiguration()




    