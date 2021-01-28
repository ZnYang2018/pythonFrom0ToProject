import time
from multiprocessing import Queue
from multiprocessing.context import Process


def write_task(q: Queue):
    if not q.full():
        for i in range(5):
            message = 'message%d' % i
            q.put(message)
            print('write in %s' % message)


def read_task(q: Queue):
    time.sleep(1)
    while not q.empty():
        print('read %s' % q.get(True, 2))


if __name__ == '__main__':
    print('----Main process starts----')
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('----Main process ends----')
