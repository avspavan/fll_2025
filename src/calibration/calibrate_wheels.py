from ..hardware import init
from ..motion import drive_straight_cm,turn_in_place_deg

def main():
    init(); drive_straight_cm(50,30); turn_in_place_deg(90,20); turn_in_place_deg(-90,20)
    print('[CAL] Tune WHEEL_CIRCUMFERENCE_CM and TURN_FACTOR_DEG_PER_DEG in config.py')

if __name__=='__main__': main()
