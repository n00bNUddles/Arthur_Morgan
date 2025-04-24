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
        # Get D-Pad state and determine motor speed in one step
        dpad_state = self.controller.getPOV()
        motor_speed = self.SPEED if dpad_state == 90 else -self.SPEED if dpad_state == 270 else 0.0

        # Set motor to calculated speed
        self.motor.set_control(DutyCycleOut(motor_speed))
