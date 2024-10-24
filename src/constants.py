from enum import (IntEnum, auto)

#region RoboRio Constants
# included to help with communication and readability
class Rio_DIO(IntEnum):
    ZERRO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    # TODO figure out how CAN works..
    TEN = auto()
    ELEVEN = auto()
    TWELVE = auto()
    THIRTEEN = auto()
    FOURTEEN = auto()
    FIFTEEN = auto()
    SIXTEEN = auto()
    SEVENTEEN = auto()

class Rio_Pnue(IntEnum):
    ZERRO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()


class Rio_PWM(IntEnum):
    ONE = 0
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()

class Rio_Relay(IntEnum):
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()

class Rio_Analog(IntEnum):
    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
#endregion

#region CAN Constants
class CAN_Address(IntEnum):
    ZERRO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    ELEVEN = auto()
    TWELVE = auto()
    THIRTEEN = auto()
    FOURTEEN = auto()
    FIFTEEN = auto()
    SIXTEEN = auto()
    SEVENTEEN = auto()
    EIGHTEEN = auto()
    NINETEEN = auto()
    TWENTY = auto()

#endregion

class DriveConstant:
    # Ports for Purple Haze 10/24/2024 (not all captured)
    kLeftMotorFront_DrivePort = CAN_Address.TWO
    kLeftMotorBack_DrivePort = CAN_Address.FOUR
    kRightMotorFront_DrivePort = CAN_Address.EIGHT
    kRightMotorBack_DrivePort = CAN_Address.SIX
    kclimbMotorPort = CAN_Address.TEN

    kLeftMotorFront_SteerPort = CAN_Address.ONE 
    kLeftMotorBack_SteerPort = CAN_Address.THREE
    kRightMotorFront_SteerPort = CAN_Address.SEVEN
    kRightMotorBack_SteerPort = CAN_Address.FIVE

    kLeftAimingMotorPort = CAN_Address.FIFTEEN
    kRightAimingMotorPort = CAN_Address.FOURTEEN





class OIConstant:
    kDriver1ControllerPort = 0
    kDriver2ControllerPort = 1