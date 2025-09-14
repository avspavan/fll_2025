"""
config.py — All constants, ports, and feature flags.

Think of this as the "settings panel" for your robot.
Students can toggle sensors ON/OFF and adjust calibration constants.
"""

# ---- PORTS ----
# Each letter matches the hub port where a motor/sensor is plugged in.
PORT_LEFT_MOTOR  = 'B'
PORT_RIGHT_MOTOR = 'C'
PORT_ARM_MOTOR   = 'A'
PORT_COLOR_SENSOR    = 'D'
PORT_DISTANCE_SENSOR = 'E'
PORT_FORCE_SENSOR    = 'F'

# ---- FEATURE FLAGS ----
# Turn sensors ON/OFF depending on availability or experiment design.
USE_GYRO            = True
USE_COLOR_SENSOR    = True
USE_DISTANCE_SENSOR = True
USE_FORCE_SENSOR    = False

# ---- CALIBRATION CONSTANTS ----
WHEEL_CIRCUMFERENCE_CM = 17.6   # Distance per wheel rotation
TURN_FACTOR_DEG_PER_DEG = 0.95  # How much wheels must rotate per robot degree turn

# ---- LINE FOLLOW CONSTANTS ----
LINE_TARGET = 50   # midpoint between white and black reflectance
LINE_KP     = 0.35 # proportional gain for line-follow steering

# ---- DISTANCE SENSOR CONSTANTS ----
WALL_APPROACH_CM = 8.0

# ---- DEFAULT MOTION SPEEDS ----
DEFAULT_SPEED = 35
SLOW_SPEED    = 20

# ---- TIMEOUTS & RETRIES ----
STEP_TIMEOUT_S = 4.0
MAX_RETRIES    = 1

# ---- LOGGING ----
VERBOSE = True
