import wpilib

class PneumaticsModule:
    def __init__(self):
        self.pcm = wpilib.PneumaticsControlModule()

        # Assuming getSolenoids returns a list or an array
        solenoids = self.pcm.getSolenoids()
        if solenoids:
            self.solenoid0 = solenoids[0]  # Access the first solenoid
        else:
            self.solenoid0 = None

    def activate_solenoid(self):
        if self.solenoid0:
            self.solenoid0.set(True)

    def deactivate_solenoid(self):
        if self.solenoid0:
            self.solenoid0.set(False)