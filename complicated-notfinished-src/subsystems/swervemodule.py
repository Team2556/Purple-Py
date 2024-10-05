import wpilib
from wpimath.kinematics import SwerveModulePosition, SwerveModuleState
from wpimath.geometry import Translation2d, Rotation2d
from wpimath.controller import PIDController, ProfiledPIDController, SimpleMotorFeedforwardMeters
from robotpy import wpilib
from phoenix6.hardware import TalonFX as DriveMotor
# from phoenix5 import TalonSRX as TurningMotor
from rev import CANSparkMax as TurningMotor
from wpimath.controller import PIDController, SimpleMotorFeedforwardMeters
from wpilib import Encoder
# from wpimath.trajectory import TrapezoidProfile

# from constants import SwerveModuleConstants

class SwerveModule:
    def __init__(self, 
                 driveMotor: DriveMotor, 
                 turningMotor: TurningMotor, 
                 driveEncoder: Encoder, 
                 turningEncoder: Encoder, 
                 drivePID: PIDController, 
                 turningPID: PIDController, 
                 driveFeedforward: SimpleMotorFeedforwardMeters, 
                 turningFeedforward: SimpleMotorFeedforwardMeters, 
                 driveEncoderDistancePerPulse: float, 
                 turningEncoderDistancePerPulse: float, 
                 driveEncoderReversed: bool, 
                 turningEncoderReversed: bool, 
                 driveEncoderPositionTolerance: float, 
                 turningEncoderPositionTolerance: float):
        self.driveMotor = driveMotor
        self.turningMotor = turningMotor
        self.driveEncoder = driveEncoder
        self.turningEncoder = turningEncoder
        self.drivePID = drivePID
        self.turningPID = turningPID
        self.driveFeedforward = driveFeedforward
        self.turningFeedforward = turningFeedforward
        self.driveEncoderDistancePerPulse = driveEncoderDistancePerPulse
        self.turningEncoderDistancePerPulse = turningEncoderDistancePerPulse
        self.driveEncoderReversed = driveEncoderReversed
        self.turningEncoderReversed = turningEncoderReversed
        self.driveEncoderPositionTolerance = driveEncoderPositionTolerance
        self.turningEncoderPositionTolerance = turningEncoderPositionTolerance

        self.driveEncoder.setDistancePerPulse(self.driveEncoderDistancePerPulse)
        self.turningEncoder.setDistancePerPulse(self.turningEncoderDistancePerPulse)

        self.drivePID.setTolerance(self.driveEncoderPositionTolerance)
        self.turningPID.setTolerance(self.turningEncoderPositionTolerance)

    def setDesiredState(self, desiredState: SwerveModuleState):
        driveOutput = self.drivePID.calculate(self.driveEncoder.getDistance(), desiredState.speedMetersPerSecond)
        turningOutput = self.turningPID.calculate(self.turningEncoder.getDistance(), desiredState.angle.radians)

        driveFeedforward = self.driveFeedforward.calculate(desiredState.speedMetersPerSecond)
        turningFeedforward = self.turningFeedforward.calculate(desiredState.angle.radians)

        self.driveMotor.setVoltage(driveOutput + driveFeedforward)
        self.turningMotor.setVoltage(turningOutput + turningFeedforward)

    def getState(self) -> SwerveModuleState:
        return SwerveModuleState(self.driveEncoder.getDistance(), Rotation2d.fromDegrees(self.turningEncoder.getDistance()))

    def resetEncoders(self):
        self.driveEncoder.reset()
        self.turningEncoder.reset()

    def getModulePosition(self) -> SwerveModulePosition:
        return SwerveModulePosition(self.getState(), Translation2d(), self.driveEncoderReversed, self.turningEncoderReversed)

    def getDriveEncoder(self) -> Encoder:
        return self.driveEncoder
    
    def getTurningEncoder(self) -> Encoder:
        return self.turningEncoder
    
    def getDrivePID(self) -> PIDController:
        return self.drivePID
    
    def getTurningPID(self) -> PIDController:
        return self.turningPID  
    