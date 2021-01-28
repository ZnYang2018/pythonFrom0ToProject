from multiprocessing import Queue
from queue import Full

if __name__ == '__main__':
    q = Queue(3)
    q.put('message1')
    q.put('message2')
    print(q.full())
    q.put('message3')
    print(q.full())

    try:
        q.put('message4', True, 2)
    except Full as e:
        print('queue is full, message count is %s' % q.qsize())

    try:
        q.put_nowait('message4')
    except:
        print('queue is full, message count is %s' % q.qsize())

    if not q.empty():
        print('get messages from queue')
        for i in range(q.qsize()):
            print(q.get_nowait())

    if not q.full():
        q.put_nowait('message4')
