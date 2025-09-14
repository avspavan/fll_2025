from .hardware import init
from .missions.mission_state_machine import run as mission_sm
def main():
    init(); mission_sm()
if __name__=='__main__': main()
