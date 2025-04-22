import wpilib
from wpilib import XboxController

class PneumaticsModule:
    def __init__(self):
        self.pcm = wpilib.PneumaticsControlModule()

        # Assuming getSolenoids returns a list or an array
        solenoids = self.pcm.getSolenoids()
        if solenoids and len(solenoids) > 1:
            self.solenoid0 = solenoids[0]  # Access solenoid 0
            self.solenoid1 = solenoids[1]  # Access solenoid 1
        else:
            self.solenoid0 = None
            self.solenoid1 = None

        # Block solenoids 0 and 1 initially
        self.block_solenoids()

        # Initialize Xbox controller
        self.controller = XboxController(0)  # Assuming controller is on port 0

    def block_solenoids(self):
        if self.solenoid0:
            self.solenoid0.set(False)
        if self.solenoid1:
            self.solenoid1.set(False)

    def handle_controller_input(self):
        # Check if the "A" button is pressed
        if self.controller.getAButton():
            self.release_solenoid0()
        else:
            self.block_solenoids()

    def release_solenoid0(self):
        if self.solenoid0:
            self.solenoid0.set(True)

    def periodic(self):
        # This method should be called periodically (e.g., in a robot loop)
        self.handle_controller_input()