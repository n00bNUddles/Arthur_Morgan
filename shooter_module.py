import math
from phoenix6.hardware import TalonFX
from phoenix6.controls import DutyCycleOut

class shooter:
    def __init__(self, motor, controller, speed=0.5):
        self.motor = motor
        self.controller = controller
        self.SPEED = speed

    def update_shooter(self):
        """Update shooter motor based on button inputs."""
        # Get button states
        a_pressed = self.controller.getAButton()
        b_pressed = self.controller.getBButton()

        # Determine motor speed based on button inputs
        motor_speed = 0.0
        if a_pressed:
            motor_speed = self.SPEED
        elif b_pressed:
            motor_speed = -self.SPEED

        # Set motor to calculated speed
        self.motor.set_control(DutyCycleOut(motor_speed))
