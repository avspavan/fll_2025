# Quick Start (Step-by-Step)
1. Open SPIKE App → New Python project.
2. Drag in the **`src/`** folder (keep structure).
3. In `config.py`, check:
   - Correct motor ports (A/B/C)
   - Correct sensor ports (D/E/F)
   - Set `USE_COLOR_SENSOR`, `USE_DISTANCE_SENSOR`, etc.
4. Run calibration scripts:
   - `calibration/calibrate_wheels.py`
   - `calibration/measure_reflectance.py`
5. Run `main.py`.
6. Switch between missions by editing `main.py`.
