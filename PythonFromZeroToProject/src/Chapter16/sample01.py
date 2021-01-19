# from multiprocessing import Process
from multiprocessing.context import Process
from multiprocessing import Process


def test(interval):
    print('我是子进程')


def main():
    print('主进程开始')
    p = Process(target=test, args=(1,))
    p.start()
    print(p.is_alive())
    print('主进程结束')
    print(p.is_alive())
    print(p.is_alive())


if __name__ == '__main__':
    main()
