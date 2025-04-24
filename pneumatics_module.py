import wpilib
from wpilib import XboxController, DoubleSolenoid

class pneumatic:
    def __init__(self):
        # Initialize REV Pneumatic Hub (CAN ID 3)
        self.ph = wpilib.PneumaticHub(3)  # REV Pneumatic Hub
        
        # Initialize solenoids with specific channels
        # Format: DoubleSolenoid(module, moduleType, forwardChannel, reverseChannel)
        self.solenoid = DoubleSolenoid(
            3,  # Module number (CAN ID)
            wpilib.PneumaticsModuleType.REVPH,  # Use REV PH
            0,  # Forward channel
            1   # Reverse channel
        )
        
        # Initialize Xbox controller
        self.controller = XboxController(0)  # Assuming controller is on port 0
        
        # Set initial state to off
        self.solenoid.set(DoubleSolenoid.Value.kOff)

        # Enable compressor with digital pressure switch
        self.ph.enableCompressorDigital()

        # Pressure thresholds
        self.MIN_PRESSURE = 60  # PSI
        self.MAX_PRESSURE = 80  # PSI

    def get_pressure(self):
        """Get the current pressure in PSI from the PH's pressure sensor."""
        return self.ph.getPressure(0)  # Analog channel 0 for pressure sensor

    def is_compressor_enabled(self):
        """Check if the compressor is currently running."""
        return self.ph.getCompressor()

    def handle_controller_input(self):
        current_pressure = self.get_pressure()
        
        # Only allow venting if pressure is above minimum
        if self.controller.getAButton() and current_pressure >= self.MIN_PRESSURE:
            # Vent through forward port
            self.solenoid.set(DoubleSolenoid.Value.kForward)
        else:
            # Close both ports to maintain pressure
            self.solenoid.set(DoubleSolenoid.Value.kOff)

    def periodic(self):
        # This method should be called periodically (e.g., in a robot loop)
        self.handle_controller_input()
        
        # Log pressure and compressor state
        pressure = self.get_pressure()
        compressor_running = self.is_compressor_enabled()
        
        # Update SmartDashboard
        wpilib.SmartDashboard.putNumber("Pneumatics Pressure (PSI)", pressure)
        wpilib.SmartDashboard.putBoolean("Compressor Running", compressor_running)
        wpilib.SmartDashboard.putBoolean("Ready to Vent", pressure >= self.MIN_PRESSURE)
        
        # Log warning if pressure is too low
        if pressure < self.MIN_PRESSURE:
            wpilib.SmartDashboard.putString("Pressure Warning", "Pressure too low! Waiting for compressor...")
        else:
            wpilib.SmartDashboard.putString("Pressure Warning", "")