import math
from phoenix6.hardware import TalonFX
from phoenix6.controls import DutyCycleOut

class drive:
    def __init__(self, motor1, motor2, controller, deadzone=0.1, turn_sensitivity=0.5):
        self.motor1 = motor1
        self.motor2 = motor2
        self.controller = controller
        self.DEADZONE = deadzone
        self.TURN_SENSITIVITY = turn_sensitivity

    def calculate_speed(self, joystick_value):
        """
        Calculate motor speed based on joystick position.
        Maps joystick values to a speed range of 0 to 1.
        """
        # Remove deadzone
        adjusted_value = (abs(joystick_value) - self.DEADZONE) / (1 - self.DEADZONE)
        # Square the value for more precise control
        adjusted_value = math.copysign(adjusted_value ** 2, joystick_value)
        # Ensure the value is between -1 and 1
        return max(-1, min(1, adjusted_value))

    def update_drive(self):
        """Update motor speeds based on joystick input."""
        # Get the left joystick values
        left_y = -self.controller.getLeftY()  # Negate to make forward positive
        left_x = self.controller.getLeftX()

        # Get the right joystick X-axis value for additional turning
        right_x = self.controller.getRightX()

        # Apply deadzone and calculate speeds
        forward_speed = self.calculate_speed(left_y) if abs(left_y) > self.DEADZONE else 0
        turn_speed = self.calculate_speed(left_x) if abs(left_x) > self.DEADZONE else 0
        additional_turn = self.calculate_speed(right_x) if abs(right_x) > self.DEADZONE else 0

        # Combine turning inputs and apply sensitivity
        total_turn = (turn_speed + additional_turn) * self.TURN_SENSITIVITY

        # Calculate and clamp final motor speeds in one step
        left_motor_speed = max(-1, min(1, forward_speed + total_turn))
        right_motor_speed = max(-1, min(1, forward_speed - total_turn))

        # Set motors to calculated speeds
        self.motor1.set_control(DutyCycleOut(left_motor_speed))
        self.motor2.set_control(DutyCycleOut(right_motor_speed))
