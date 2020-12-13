# 在CMD输出彩色文字 pip install colorama
from colorama import init, Fore, Style, Back

if __name__ == '__main__':
    init(autoreset=True)
    print('\033[32m绿色')
    print(Fore.RED + '红色')
    print(Fore.GREEN + 'Green')
    print(Fore.LIGHTMAGENTA_EX + '紫色')
    print('haha')
    print(Style.DIM + 'DefaultColor')

    # 若未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    print('back to normal now')
