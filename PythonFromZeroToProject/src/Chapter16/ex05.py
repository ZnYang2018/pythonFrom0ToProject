import os
from multiprocessing.context import Process


def process_func1(param):
    print('in fun1 param, pid and ppid are:', param, os.getpid(), os.getppid())


def process_func2(param):
    print('in fun2 param, pid and ppid are:', param, os.getpid(), os.getppid())


if __name__ == '__main__':
    print('main process starts')
    p1 = Process(target=process_func1, name='process name1', args=(1,))
    p2 = Process(target=process_func2, args=(2,))

    p1.start()
    p2.start()
    print('p1 name and pid:', p1.name, p1.pid)
    print('p2 name and pid:', p2.name, p2.pid)
    p1.join()
    p2.join()

    print('main process ends')
