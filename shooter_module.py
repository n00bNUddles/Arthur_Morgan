import math
from phoenix6.hardware import TalonFX
from phoenix6.controls import DutyCycleOut

class shooter:
    def __init__(self, motor, controller, speed=0.25):
        self.motor = motor
        self.controller = controller
        self.SPEED = speed

    def update_shooter(self):
        """Update shooter motor based on D-Pad inputs."""
        # Get D-Pad states
        dpad_left = self.controller.getPOV() == 270  # D-Pad left is 270 degrees
        dpad_right = self.controller.getPOV() == 90  # D-Pad right is 90 degrees

        # Determine motor speed based on D-Pad inputs
        motor_speed = 0.0
        if dpad_right:
            motor_speed = self.SPEED
        elif dpad_left:
            motor_speed = -self.SPEED

        # Set motor to calculated speed
        self.motor.set_control(DutyCycleOut(motor_speed))
