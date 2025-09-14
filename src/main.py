"""
main.py — entry point; init hardware then run a mission.
MIT License.
"""
from .hardware import init
from .config import VERBOSE
from .missions.mission_state_machine import run as mission_sm
from .missions.mission1 import run as mission1

def main():
    init()
    if VERBOSE: print("[MAIN] Hardware ready.")
    # Choose which mission to run:
    # mission1()
    mission_sm()

if __name__ == "__main__":
    main()
