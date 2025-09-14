from .hardware import init
from .missions.mission1 import run as mission1

def main(): init(); mission1()
if __name__=='__main__': main()
