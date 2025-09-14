"""
calibration/calibrate_wheels.py — distance & turn calibration helper.

Procedure:
1) Command 50 cm forward on the mat; measure actual distance.
   - If it moved 47 cm, multiply WHEEL_CIRCUMFERENCE_CM by (50/47).
2) Command 90° turns (both directions); if it under/overshoots, adjust
   TURN_FACTOR_DEG_PER_DEG up/down until 90° ≈ 90° consistently.
Repeat until consistent.

MIT License.
"""
from ..hardware import init
from ..motion import drive_straight_cm, turn_in_place_deg

def main():
    init()
    print("\n[CAL] Step 1: Command 50 cm forward; measure actual.")
    drive_straight_cm(50, speed=30)
    print("[CAL] If actual != 50 cm, adjust WHEEL_CIRCUMFERENCE_CM proportionally in config.py.")

    print("\n[CAL] Step 2: Command 90° right, then 90° left; tune TURN_FACTOR_DEG_PER_DEG.")
    turn_in_place_deg(90, speed=20)
    turn_in_place_deg(-90, speed=20)
    print("[CAL] Repeat a few times and adjust until turns are spot on.")

if __name__ == "__main__":
    main()
