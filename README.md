# FLL Challenge Robot Starter Kit (SPIKE Prime, Python, Ultra-Docs)
**Audience:** FLL Challenge coaches + students new to coding and robotics  
**Purpose:** A *teaching-first* codebase with **extreme comments, diagrams, and explanations**.  
Everything is documented as if this were a tutorial book.

---
## Key Concepts Taught
- Mapping robot motors/sensors to Python objects
- Writing **functions** that control motion/attachments
- Using **optional sensors** (color, distance, force)
- Building missions as **step-by-step functions**
- Adding **auto-correct + retry** logic for reliability
- Running calibration and updating constants
- Visualizing with **flowcharts**

---
## Directory Layout
```
fll_ai_robot_kit_ultra/
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
---
## How to Use
1. Drag `src/` into your SPIKE App Python project.
2. Open `config.py`, set your **ports** and **flags**.
3. Run calibrations (wheel distance & line reflectance).
4. Test simple mission (`mission1.py`), then state machine (`mission_state_machine.py`).
5. Iterate with students: adjust constants, try retries, explore flowcharts.

---
