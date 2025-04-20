import wpilib
from pneumatics_module import PneumaticsModule
from drive_module import drive
from phoenix6.hardware import TalonFX

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize motors (TalonFX)
        self.motor1 = TalonFX(1)
        self.motor2 = TalonFX(2)

        # Initialize Xbox Controller (assuming 0 as the port)
        self.controller = wpilib.XboxController(0)

        # Create Drive object with motors and controller
        self.drive = drive(self.motor1, self.motor2, self.controller)

        # Initialize pneumatics system
        self.pneumatics = PneumaticsModule()

    def teleopPeriodic(self):
        # Update the drive based on joystick input
        self.drive.update_drive()
        