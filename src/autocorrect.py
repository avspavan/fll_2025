"""Auto-correct ultra-docs"""
from .line_follow import drive_until_black
from .motion import square_to_wall
def auto_correct():
    if not drive_until_black(speed=20,timeout_s=1.5): square_to_wall()
