import os
import time
from multiprocessing import Lock, Process, Value

def square_numbers():
    for i in range(100):

        _ = i * i
        time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()

# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# for p in processes:
#     p.start()

# for p in processes:
#     p.join()

# print('end main')


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        with lock:
            number.value += 1
        # lock.release()

if __name__ == "__main__":
    shared_number = Value('i',0)
    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)
 
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print('end main')

    lock = Lock()
    shared_number = Value('i',0)
    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is ',shared_number.value)

