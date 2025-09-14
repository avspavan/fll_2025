# Quick Start
1. Create a SPIKE Python project; drag the entire `src/` folder into it.
2. Edit `src/config.py`:
   - Set your motor ports (A/B/C) and sensor ports (D/E/F).
   - Toggle `USE_COLOR_SENSOR`, `USE_DISTANCE_SENSOR`, etc.
3. Calibration:
   - Run `src/calibration/calibrate_wheels.py` to tune distances/turns.
   - Run `src/calibration/measure_reflectance.py` to set `LINE_TARGET`.
4. Run `src/main.py` to execute the robust state-machine mission.
5. Switch to the simpler mission by editing `main.py` and calling `mission1()`.
