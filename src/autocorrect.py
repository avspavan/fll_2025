
from .config import *
from .line_follow import drive_until_black
from .motion import square_to_wall, drive_straight_cm
def step_with_retries(step_fn,max_retries=MAX_RETRIES):
    for a in range(max_retries+1):
        if step_fn(): return True
        auto_correct()
    return False
def auto_correct():
    if not drive_until_black(speed=20,timeout_s=1.5):
        square_to_wall()
def fallback_home():
    square_to_wall(); drive_straight_cm(-45, speed=DEFAULT_SPEED)
