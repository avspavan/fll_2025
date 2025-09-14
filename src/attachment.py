from .hardware import arm_motor
from .config import DEFAULT_SPEED

def arm_up(deg=120,speed=DEFAULT_SPEED): arm_motor.run_for_degrees(abs(deg),speed)

def arm_down(deg=120,speed=DEFAULT_SPEED): arm_motor.run_for_degrees(-abs(deg),speed)
