
from .config import *
from spike import PrimeHub, Motor, MotorPair, ColorSensor, DistanceSensor, ForceSensor
hub=PrimeHub()
left_motor=Motor(PORT_LEFT_MOTOR); right_motor=Motor(PORT_RIGHT_MOTOR)
drive_pair=MotorPair(PORT_LEFT_MOTOR, PORT_RIGHT_MOTOR); arm_motor=Motor(PORT_ARM_MOTOR)
color_sensor=ColorSensor(PORT_COLOR_SENSOR) if USE_COLOR_SENSOR else None
distance_sensor=DistanceSensor(PORT_DISTANCE_SENSOR) if USE_DISTANCE_SENSOR else None
force_sensor=ForceSensor(PORT_FORCE_SENSOR) if USE_FORCE_SENSOR else None
def init(): pass
def has_color(): return color_sensor is not None
def has_distance(): return distance_sensor is not None
def has_force(): return force_sensor is not None
def safe_get_color(): return color_sensor.get_color() if has_color() else None
def safe_get_reflected(): return color_sensor.get_reflected_light() if has_color() else 50
def safe_get_distance_cm(): return distance_sensor.get_distance_cm() if has_distance() else 999
def reset_yaw(): hub.motion_sensor.reset_yaw_angle()
def get_yaw(): return hub.motion_sensor.get_yaw_angle()
