import wpilib
from pneumatics_module import PneumaticsModule
from drive_module import drive
from shooter_module import shooter
from phoenix6.hardware import TalonFX

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize motors (TalonFX)
        self.motor1 = TalonFX(1)
        self.motor2 = TalonFX(2)
        self.shooter_motor = TalonFX(4)  # Add shooter motor

        # Initialize Xbox Controller (assuming 0 as the port)
        self.controller = wpilib.XboxController(0)

        # Create Drive object with motors and controller
        self.drive = drive(self.motor1, self.motor2, self.controller)

        # Initialize pneumatics system
        self.pneumatics = PneumaticsModule()

        # Initialize shooter system
        self.shooter = shooter(self.shooter_motor, self.controller)

    def teleopPeriodic(self):
        # Update the drive based on joystick input
        self.drive.update_drive()

        # Update the pneumatics system
        self.pneumatics.periodic()

        # Update the shooter system
        self.shooter.update_shooter()