from .config import *
from .hardware import hub,left_motor,right_motor,drive_pair,reset_yaw,get_yaw,safe_get_distance_cm,has_distance
from time import sleep,time
def drive_straight_cm(cm,speed=DEFAULT_SPEED,kp=2.0):
    target_deg=(cm/WHEEL_CIRCUMFERENCE_CM)*360; left_motor.set_degrees_counted(0); reset_yaw()
    drive_pair.start(0,speed if cm>=0 else -speed)
    while abs(left_motor.get_degrees_counted())<abs(target_deg):
        steer=int(-get_yaw()*kp) if USE_GYRO else 0
        drive_pair.start(steer, speed if cm>=0 else -speed)
    drive_pair.stop()
def turn_in_place_deg(deg,speed=SLOW_SPEED):
    wheel_deg=abs(deg)*TURN_FACTOR_DEG_PER_DEG
    if deg>0:
        left_motor.run_for_degrees(int(wheel_deg),speed); right_motor.run_for_degrees(-int(wheel_deg),speed)
    else:
        left_motor.run_for_degrees(-int(wheel_deg),speed); right_motor.run_for_degrees(int(wheel_deg),speed)
def square_to_wall(bump_ms=300,back_cm=4,speed=SLOW_SPEED):
    drive_pair.start(0,speed); sleep(bump_ms/1000); drive_pair.stop(); reset_yaw(); drive_straight_cm(-abs(back_cm),max(20,speed))
