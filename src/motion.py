"""
motion.py — motion primitives: drive straight, turn, square to wall, drive until wall.
Uses encoders; adds gyro-based heading correction if enabled.

MIT License.
"""
from time import sleep, time
from .config import (
    WHEEL_CIRCUMFERENCE_CM, TURN_FACTOR_DEG_PER_DEG,
    DEFAULT_SPEED, SLOW_SPEED, WALL_APPROACH_CM, USE_GYRO, VERBOSE
)
from .hardware import (
    hub, left_motor, right_motor, drive_pair,
    reset_yaw, get_yaw, safe_get_distance_cm, has_distance
)

def drive_straight_cm(distance_cm, speed=DEFAULT_SPEED, kp=2.0):
    """
    Drive straight for distance_cm (positive forward, negative backward).
    If gyro is on, apply P-control to hold yaw≈0° while driving.
    """
    if VERBOSE: print(f"[MOVE] drive_straight_cm {distance_cm}cm @ {speed}% (gyro={'on' if USE_GYRO else 'off'})")
    target_deg = (abs(distance_cm) / WHEEL_CIRCUMFERENCE_CM) * 360.0
    left_motor.set_degrees_counted(0)
    right_motor.set_degrees_counted(0)
    direction = 1 if distance_cm >= 0 else -1

    if USE_GYRO:
        reset_yaw()

    drive_pair.start(0, direction * abs(speed))
    while abs(left_motor.get_degrees_counted()) < target_deg:
        steer = 0
        if USE_GYRO:
            error = -get_yaw()  # want 0
            steer = max(min(int(kp * error), 100), -100)
        drive_pair.start(steer, direction * abs(speed))
    drive_pair.stop()

def turn_in_place_deg(degrees, speed=SLOW_SPEED):
    """
    Turn in place by 'degrees' (right positive, left negative).
    Encoder-based; tune TURN_FACTOR_DEG_PER_DEG in config for your chassis.
    """
    if VERBOSE: print(f"[MOVE] turn_in_place_deg {degrees}° @ {speed}%")
    wheel_deg = abs(degrees) * TURN_FACTOR_DEG_PER_DEG
    if degrees > 0:
        left_motor.run_for_degrees( int(wheel_deg),  speed)
        right_motor.run_for_degrees(-int(wheel_deg), speed)
    else:
        left_motor.run_for_degrees(-int(wheel_deg), speed)
        right_motor.run_for_degrees( int(wheel_deg), speed)

def drive_until_wall(speed=DEFAULT_SPEED, min_cm=WALL_APPROACH_CM, timeout_s=4.0):
    """
    Drive forward until distance sensor reads <= min_cm, or timeout.
    Returns True on success, False if sensor unavailable or timeout.
    """
    if VERBOSE: print(f"[MOVE] drive_until_wall to {min_cm}cm @ {speed}%")
    if not has_distance():
        if VERBOSE: print("[WARN] Distance sensor not enabled/available.")
        return False
    start = time()
    drive_pair.start(0, speed)
    while time() - start < timeout_s:
        d = safe_get_distance_cm()
        if d <= min_cm:
            drive_pair.stop()
            return True
    drive_pair.stop()
    return False

def square_to_wall(bump_ms=300, back_cm=4, speed=SLOW_SPEED):
    """
    Gentle bump to wall to square chassis; then back off a fixed distance.
    Resets yaw after the bump; useful as a 'checkpoint' to correct drift.
    """
    if VERBOSE: print(f"[MOVE] square_to_wall bump {bump_ms}ms, back {back_cm}cm")
    drive_pair.start(0, speed); sleep(bump_ms/1000.0); drive_pair.stop()
    reset_yaw()
    drive_straight_cm(-abs(back_cm), speed=max(20, speed))
