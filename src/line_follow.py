
from .config import *
from .hardware import drive_pair,left_motor,has_color,safe_get_color,safe_get_reflected
from time import time
def drive_until_black(speed=DEFAULT_SPEED,timeout_s=STEP_TIMEOUT_S):
    if not has_color(): return False
    t=time(); drive_pair.start(0,speed)
    while time()-t<timeout_s:
        if safe_get_color()=='black': drive_pair.stop(); return True
    drive_pair.stop(); return False
def line_follow_cm(cm,base=DEFAULT_SPEED,target=LINE_TARGET,kp=LINE_KP):
    left_motor.set_degrees_counted(0); from .config import WHEEL_CIRCUMFERENCE_CM
    target_deg=(abs(cm)/WHEEL_CIRCUMFERENCE_CM)*360; direction=1 if cm>=0 else -1
    while abs(left_motor.get_degrees_counted())<target_deg:
        steer=int(kp*(target-safe_get_reflected())) if has_color() else 0
        drive_pair.start(steer, direction*abs(base))
    drive_pair.stop()
