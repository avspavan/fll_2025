"""
calibration/measure_reflectance.py — find white/black reflectance and suggest LINE_TARGET.
MIT License.
"""
from ..hardware import init, has_color, safe_get_reflected

def main():
    init()
    if not has_color():
        print("[CAL] Color sensor not enabled/available. Enable in config.py and check port.")
        return
    input("[CAL] Place sensor over WHITE area, then press Enter...")
    white = safe_get_reflected()
    input("[CAL] Place sensor over BLACK line, then press Enter...")
    black = safe_get_reflected()
    target = (white + black) // 2
    print(f"[CAL] WHITE={white}, BLACK={black}, Suggested LINE_TARGET={target}")
    print("[CAL] Set LINE_TARGET in config.py to this value.")

if __name__ == "__main__":
    main()
