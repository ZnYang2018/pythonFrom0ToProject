import os
import time
from multiprocessing.pool import Pool


def task(name):
    print('子进程(%s)执行task %s ...' % (os.getpid(), name))
    time.sleep(1)


if __name__ == '__main__':
    print('父进程(%s).' % os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task, args=(i,))
    print('等待所有子进程结束...')
    p.close()
    p.join()
    print('所有子进程结束.')
