from .hardware import init
from .missions.mission_state_machine import run as mission_sm
from .missions.mission1 import run as mission1

def main():
    init(); mission_sm()

if __name__=='__main__': main()
