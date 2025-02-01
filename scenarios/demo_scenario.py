from devices.motor_driver import MotorDriver
import time

class DemoScenario:
    def __init__(self):
        # Initialize motor with PWM control
        self.motor = MotorDriver(
            enable_pin=12,  # PWM pin
            in1_pin=14,
            in2_pin=27
        )

    def run(self):
        # Smooth acceleration demo
        for speed in range(0, 101, 10):
            self.motor.clockwise(speed)
            time.sleep(0.5)
        
        self.motor.stop()
        time.sleep(1)
        
        # Reverse direction
        self.motor.counterclockwise(75)
        time.sleep(2)
        self.motor.stop()