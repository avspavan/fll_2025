"""
motion.py — Core driving primitives.

Functions here abstract basic movements:
- drive_straight_cm
- turn_in_place_deg
- drive_until_wall
- square_to_wall
"""
from .config import *
from .hardware import hub,left_motor,right_motor,drive_pair,reset_yaw,get_yaw,safe_get_distance_cm,has_distance
from time import sleep,time

def drive_straight_cm(cm, speed=DEFAULT_SPEED, kp=2.0):
    """
    Drive straight for cm.
    If gyro enabled, apply proportional correction to keep heading = 0.
    """
    if VERBOSE: print(f"[MOVE] Driving {cm}cm @ {speed}%")
    target_deg=(abs(cm)/WHEEL_CIRCUMFERENCE_CM)*360
    left_motor.set_degrees_counted(0)
    reset_yaw()
    direction = 1 if cm>=0 else -1
    drive_pair.start(0, direction*speed)
    while abs(left_motor.get_degrees_counted())<target_deg:
        steer=int(-get_yaw()*kp) if USE_GYRO else 0
        drive_pair.start(steer, direction*speed)
    drive_pair.stop()

def turn_in_place_deg(deg, speed=SLOW_SPEED):
    """Turn robot in place by deg (right positive, left negative)."""
    if VERBOSE: print(f"[MOVE] Turning {deg}°")
    wheel_deg=abs(deg)*TURN_FACTOR_DEG_PER_DEG
    if deg>0:
        left_motor.run_for_degrees(int(wheel_deg),speed)
        right_motor.run_for_degrees(-int(wheel_deg),speed)
    else:
        left_motor.run_for_degrees(-int(wheel_deg),speed)
        right_motor.run_for_degrees(int(wheel_deg),speed)

def drive_until_wall(speed=DEFAULT_SPEED,min_cm=WALL_APPROACH_CM,timeout_s=4.0):
    """Drive forward until distance <= min_cm, or timeout."""
    if not has_distance(): return False
    t=time(); drive_pair.start(0,speed)
    while time()-t<timeout_s:
        if safe_get_distance_cm()<=min_cm:
            drive_pair.stop(); return True
    drive_pair.stop(); return False

def square_to_wall(bump_ms=300,back_cm=4,speed=SLOW_SPEED):
    """Bump wall to align, back up, reset yaw."""
    drive_pair.start(0,speed); sleep(bump_ms/1000); drive_pair.stop()
    reset_yaw(); drive_straight_cm(-abs(back_cm),max(20,speed))
