"""
missions/mission_state_machine.py — robust mission with retries + auto-correct.
MIT License.
"""
from time import sleep
from ..config import VERBOSE
from ..autocorrect import step_with_retries, fallback_home
from ..motion import drive_straight_cm, turn_in_place_deg, square_to_wall
from ..line_follow import drive_until_black, line_follow_cm
from ..attachment import arm_down, arm_up
from ..hardware import has_color

def step_drive_to_line():
    return drive_until_black()

def step_line_to_target():
    line_follow_cm(30, base=25)
    return True

def step_do_attachment():
    arm_down(120); sleep(0.2); arm_up(120)
    return True

def step_return():
    square_to_wall()
    drive_straight_cm(-35, speed=30)
    return True

def run():
    if VERBOSE: print("[MISSION] mission_state_machine")
    if not step_with_retries(step_drive_to_line, max_retries=1):
        return fallback_home()
    if not step_with_retries(step_line_to_target, max_retries=1):
        return fallback_home()
    step_with_retries(step_do_attachment, max_retries=0)
    if not step_with_retries(step_return, max_retries=1):
        return fallback_home()
