# FLL Challenge Robot Starter Kit (SPIKE Prime, Python) — Executable + Heavily Commented
This package contains **real, runnable code** with **detailed comments** (no placeholders).
Import the whole `src/` folder into the SPIKE App (Python). Keep subfolders intact.

## Directory
```
fll_ai_robot_kit_exec/
├─ README.md
├─ docs/
│  ├─ QUICK_START.md
│  └─ flowcharts/
│     ├─ mission_state_machine.mmd
│     └─ data_flow.mmd
└─ src/
   ├─ config.py
   ├─ hardware.py
   ├─ motion.py
   ├─ line_follow.py
   ├─ attachment.py
   ├─ autocorrect.py
   ├─ main.py
   ├─ missions/
   │  ├─ mission1.py
   │  └─ mission_state_machine.py
   └─ calibration/
      ├─ calibrate_wheels.py
      └─ measure_reflectance.py
```

## Quick Start
1) Drag **`src/`** into a SPIKE Python project.  
2) Open `config.py`, set ports + sensor flags.  
3) Run `src/calibration/calibrate_wheels.py` and `src/calibration/measure_reflectance.py`.  
4) Put robot at Base and run `src/main.py`.
