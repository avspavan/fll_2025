from ..hardware import init
from ..hardware import has_color, safe_get_reflected

def main():
    init()
    if not has_color():
        print('[CAL] Enable color sensor in config.py and check port.')
        return
    input('[CAL] Place over WHITE and press Enter...')
    white=safe_get_reflected()
    input('[CAL] Place over BLACK and press Enter...')
    black=safe_get_reflected()
    print(f'[CAL] WHITE={white}, BLACK={black}, Suggested LINE_TARGET={(white+black)//2}')

if __name__=='__main__': main()
