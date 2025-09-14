from ..autocorrect import step_with_retries,fallback_home
from ..line_follow import drive_until_black,line_follow_cm
from ..attachment import arm_down,arm_up
from ..motion import square_to_wall, drive_straight_cm
from time import sleep

def step_drive_to_line(): return drive_until_black()

def step_line_to_target(): line_follow_cm(30, base=25); return True

def step_do_attachment(): arm_down(120); sleep(0.2); arm_up(120); return True

def step_return(): square_to_wall(); drive_straight_cm(-35, speed=30); return True

def run():
    if not step_with_retries(step_drive_to_line,1): return fallback_home()
    if not step_with_retries(step_line_to_target,1): return fallback_home()
    step_with_retries(step_do_attachment,0)
    if not step_with_retries(step_return,1): return fallback_home()
