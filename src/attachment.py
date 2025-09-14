"""
attachment.py — arm/aux motor helpers.

MIT License.
"""
from .hardware import arm_motor
from .config import DEFAULT_SPEED, VERBOSE

def arm_up(degrees=120, speed=DEFAULT_SPEED):
    if VERBOSE: print(f"[ATTACH] arm_up {degrees}deg @ {speed}%")
    arm_motor.run_for_degrees(abs(degrees), speed)

def arm_down(degrees=120, speed=DEFAULT_SPEED):
    if VERBOSE: print(f"[ATTACH] arm_down {degrees}deg @ {speed}%")
    arm_motor.run_for_degrees(-abs(degrees), speed)
