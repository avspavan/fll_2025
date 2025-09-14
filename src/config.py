"""
config.py — ports, flags, and calibration constants.
Flip flags to make sensors optional; code degrades gracefully if a sensor is disabled.

MIT License.
"""

# ---- PORTS ----
PORT_LEFT_MOTOR  = 'B'   # left wheel motor
PORT_RIGHT_MOTOR = 'C'   # right wheel motor
PORT_ARM_MOTOR   = 'A'   # attachment motor

PORT_COLOR_SENSOR    = 'D'   # optional
PORT_DISTANCE_SENSOR = 'E'   # optional
PORT_FORCE_SENSOR    = 'F'   # optional

# ---- FEATURE FLAGS ----
USE_GYRO            = True
USE_COLOR_SENSOR    = True
USE_DISTANCE_SENSOR = True
USE_FORCE_SENSOR    = False

# ---- CALIBRATION ----
WHEEL_CIRCUMFERENCE_CM   = 17.6  # cm per wheel rotation (56mm SPIKE wheel)
TURN_FACTOR_DEG_PER_DEG  = 0.95  # wheel degrees per robot degree (empirical)

# ---- LINE FOLLOW ----
LINE_TARGET = 50   # midpoint between white/black reflectance
LINE_KP     = 0.35 # proportional gain for line-follow steering

# ---- DISTANCE SENSOR ----
WALL_APPROACH_CM = 8.0

# ---- MOTION DEFAULTS ----
DEFAULT_SPEED = 35
SLOW_SPEED    = 20

# ---- TIMEOUTS & RETRIES ----
STEP_TIMEOUT_S = 4.0
MAX_RETRIES    = 1

# ---- LOGGING ----
VERBOSE = True
