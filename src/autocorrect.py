"""
autocorrect.py — auto-correction routines + step/retry scaffolding.

MIT License.
"""
from .config import STEP_TIMEOUT_S, MAX_RETRIES, VERBOSE, DEFAULT_SPEED
from .hardware import has_color
from .line_follow import drive_until_black
from .motion import drive_straight_cm, square_to_wall

def step_with_retries(step_fn, max_retries=MAX_RETRIES):
    """Run step_fn(); on failure, auto_correct() and retry up to max_retries."""
    attempts = 0
    while attempts <= max_retries:
        if VERBOSE: print(f"[STATE] {step_fn.__name__} attempt {attempts+1}/{max_retries+1}")
        if step_fn():
            return True
        auto_correct()
        attempts += 1
    return False

def auto_correct():
    """Try line reacquire; fallback to squaring to wall if that fails quickly."""
    if VERBOSE: print("[AUTO] auto_correct")
    seen = False
    if has_color():
        seen = drive_until_black(speed=20, timeout_s=1.5)
    if not seen:
        square_to_wall()

def fallback_home():
    """Return to base conservatively."""
    if VERBOSE: print("[AUTO] fallback_home")
    square_to_wall()
    drive_straight_cm(-45, speed=DEFAULT_SPEED)
