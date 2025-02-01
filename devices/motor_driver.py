from machine import Pin, PWM

class MotorDriver:
    def __init__(self, enable_pin, in1_pin, in2_pin):
        # PWM for speed control
        self.enable = PWM(Pin(enable_pin), freq=1000)
        self.enable.duty(0)  # Start stopped
        
        # Direction pins
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        
        self.current_speed = 0
        self.current_direction = "stop"

    def set_speed(self, speed_percent):
        """Set motor speed (0-100%)"""
        duty = int(1023 * (speed_percent / 100))
        self.enable.duty(duty)
        self.current_speed = speed_percent

    def clockwise(self, speed=100):
        self.in1.on()
        self.in2.off()
        self.set_speed(speed)
        self.current_direction = "cw"

    def counterclockwise(self, speed=100):
        self.in1.off()
        self.in2.on()
        self.set_speed(speed)
        self.current_direction = "ccw"

    def stop(self):
        self.enable.duty(0)
        self.current_speed = 0
        self.current_direction = "stop"

    def get_status(self):
        return {
            "speed": self.current_speed,
            "direction": self.current_direction
        }