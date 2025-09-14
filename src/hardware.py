"""
hardware.py — initialize hub, motors, sensors; expose safe accessors.
If sensors are off/missing, safe_* returns neutral values and the rest of
the code keeps running.

MIT License.
"""
from time import sleep
try:
    from spike import PrimeHub, Motor, MotorPair, ColorSensor, DistanceSensor, ForceSensor
except Exception as e:
    # Allows importing this file off-robot for reading, but real run needs SPIKE runtime.
    PrimeHub = Motor = MotorPair = ColorSensor = DistanceSensor = ForceSensor = None

from .config import (
    PORT_LEFT_MOTOR, PORT_RIGHT_MOTOR, PORT_ARM_MOTOR,
    PORT_COLOR_SENSOR, PORT_DISTANCE_SENSOR, PORT_FORCE_SENSOR,
    USE_GYRO, USE_COLOR_SENSOR, USE_DISTANCE_SENSOR, USE_FORCE_SENSOR, VERBOSE
)

# Globals
hub = None
left_motor = None
right_motor = None
drive_pair = None
arm_motor = None
color_sensor = None
distance_sensor = None
force_sensor = None

def init():
    """Call once at program start; binds hardware and optional sensors."""
    global hub, left_motor, right_motor, drive_pair, arm_motor
    global color_sensor, distance_sensor, force_sensor

    if PrimeHub is None:
        raise RuntimeError("SPIKE runtime not detected. Run on the hub or in the SPIKE App (Python).")

    hub = PrimeHub()
    left_motor  = Motor(PORT_LEFT_MOTOR)
    right_motor = Motor(PORT_RIGHT_MOTOR)
    drive_pair  = MotorPair(PORT_LEFT_MOTOR, PORT_RIGHT_MOTOR)
    arm_motor   = Motor(PORT_ARM_MOTOR)

    if USE_COLOR_SENSOR:
        try:
            color_sensor = ColorSensor(PORT_COLOR_SENSOR)
            if VERBOSE: print(f"[HW] Color sensor on {PORT_COLOR_SENSOR}")
        except Exception as e:
            color_sensor = None
            if VERBOSE: print("[HW] Color sensor not available:", e)

    if USE_DISTANCE_SENSOR:
        try:
            distance_sensor = DistanceSensor(PORT_DISTANCE_SENSOR)
            if VERBOSE: print(f"[HW] Distance sensor on {PORT_DISTANCE_SENSOR}")
        except Exception as e:
            distance_sensor = None
            if VERBOSE: print("[HW] Distance sensor not available:", e)

    if USE_FORCE_SENSOR:
        try:
            force_sensor = ForceSensor(PORT_FORCE_SENSOR)
            if VERBOSE: print(f"[HW] Force sensor on {PORT_FORCE_SENSOR}")
        except Exception as e:
            force_sensor = None
            if VERBOSE: print("[HW] Force sensor not available:", e)

def has_color():    return color_sensor is not None
def has_distance(): return distance_sensor is not None
def has_force():    return force_sensor is not None

def safe_get_color():
    """Return color name (e.g., 'black') or None if unavailable."""
    if has_color():
        try: return color_sensor.get_color()
        except: return None
    return None

def safe_get_reflected():
    """Return 0..100 reflectance or 50 if unavailable."""
    if has_color():
        try: return color_sensor.get_reflected_light()
        except: return 50
    return 50

def safe_get_distance_cm():
    """Return distance in cm or 999 if unavailable."""
    if has_distance():
        try: return distance_sensor.get_distance_cm()
        except: return 999
    return 999

def reset_yaw():
    if hub and USE_GYRO:
        try: hub.motion_sensor.reset_yaw_angle()
        except: pass

def get_yaw():
    if hub and USE_GYRO:
        try: return hub.motion_sensor.get_yaw_angle()
        except: return 0
    return 0
