"""
line_follow.py — line detection + P-controlled line following.
If color sensor is disabled/missing, functions degrade gracefully.

MIT License.
"""
from time import time
from .config import LINE_TARGET, LINE_KP, DEFAULT_SPEED, STEP_TIMEOUT_S, VERBOSE, WHEEL_CIRCUMFERENCE_CM
from .hardware import drive_pair, left_motor, has_color, safe_get_color, safe_get_reflected

def drive_until_black(speed=DEFAULT_SPEED, timeout_s=STEP_TIMEOUT_S):
    """Drive until black line detected or timeout. Return True on success."""
    if VERBOSE: print(f"[LINE] drive_until_black @ {speed}% (timeout {timeout_s}s)")
    if not has_color():
        if VERBOSE: print("[WARN] No color sensor; cannot detect black line.")
        return False
    start = time()
    drive_pair.start(0, speed)
    while time() - start < timeout_s:
        if safe_get_color() == 'black':
            drive_pair.stop()
            return True
    drive_pair.stop()
    return False

def line_follow_cm(distance_cm, base=DEFAULT_SPEED, target=LINE_TARGET, kp=LINE_KP):
    """
    Follow a line for distance_cm using proportional control around reflectance target.
    If color sensor is unavailable, this falls back to straight drive.
    """
    if VERBOSE: print(f"[LINE] line_follow_cm {distance_cm}cm @ base {base}%")
    left_motor.set_degrees_counted(0)
    target_deg = (abs(distance_cm) / WHEEL_CIRCUMFERENCE_CM) * 360.0
    direction = 1 if distance_cm >= 0 else -1

    while abs(left_motor.get_degrees_counted()) < target_deg:
        steer = 0
        if has_color():
            refl = safe_get_reflected()
            err = target - refl
            steer = int(kp * err)
        drive_pair.start(steer, direction * abs(base))
    drive_pair.stop()
