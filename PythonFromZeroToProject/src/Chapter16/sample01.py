# from multiprocessing import Process
from multiprocessing.context import Process
from multiprocessing import Process


def test(interval):
    print('我是子进程', interval)


def main():
    print('主进程开始')
    p = Process(target=test, args=(1,))
    p.start()
    print(p.is_alive())
    print('主进程结束')
    print(p.is_alive())
    print(p.is_alive())
    print(p.is_alive())
    print(p.is_alive())
    print(p.is_alive())
    print('子进程名字:', p.name)
    print('子进程pid:', p.pid)
    p.terminate()
    p.join(20)


if __name__ == '__main__':
    main()
