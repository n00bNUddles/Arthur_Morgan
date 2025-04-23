import wpilib
from wpilib import XboxController, DoubleSolenoid

class PneumaticsModule:
    def __init__(self):
        # Initialize PCM (Pneumatics Control Module)
        self.pcm = wpilib.PneumaticsControlModule()
        
        # Initialize solenoids with specific channels
        # Format: DoubleSolenoid(module, forwardChannel, reverseChannel)
        self.solenoid = DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM,  # Use CTRE PCM
            0,  # Forward channel
            1   # Reverse channel
        )
        
        # Initialize Xbox controller
        self.controller = XboxController(0)  # Assuming controller is on port 0
        
        # Set initial state to off
        self.solenoid.set(DoubleSolenoid.Value.kOff)

    def handle_controller_input(self):
        # Check if the "A" button is pressed
        if self.controller.getAButton():
            # Extend solenoid
            self.solenoid.set(DoubleSolenoid.Value.kForward)
        else:
            # Retract solenoid
            self.solenoid.set(DoubleSolenoid.Value.kReverse)

    def periodic(self):
        # This method should be called periodically (e.g., in a robot loop)
        self.handle_controller_input()