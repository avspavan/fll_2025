"""Line follow ultra-docs"""
from .config import *
from .hardware import drive_pair,left_motor,has_color,safe_get_color,safe_get_reflected
from time import time

def drive_until_black(speed=DEFAULT_SPEED,timeout_s=STEP_TIMEOUT_S):
    if not has_color(): return False
    t=time(); drive_pair.start(0,speed)
    while time()-t<timeout_s:
        if safe_get_color()=='black': drive_pair.stop(); return True
    drive_pair.stop(); return False

