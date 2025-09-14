"""
missions/mission1.py — simple linear mission demonstrating primitives.
MIT License.
"""
from time import sleep
from ..motion import drive_straight_cm, turn_in_place_deg
from ..line_follow import drive_until_black, line_follow_cm
from ..attachment import arm_down, arm_up

def run():
    # Example: leave base, find a line, follow, actuate attachment, return.
    drive_straight_cm(20)
    turn_in_place_deg(90)
    drive_until_black()
    line_follow_cm(25, base=25)
    arm_down(90); sleep(0.3); arm_up(90)
    turn_in_place_deg(-90)
    drive_straight_cm(-25)
