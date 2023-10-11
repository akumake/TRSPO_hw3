

import threading

lock = threading.Lock()

numbers = range(100, 500)

all_steps = 0

def queue_process():
    for i in range(len(numbers)):
        try:
            with lock:
                number = next(it)
            collatz_function(number)
        except StopIteration:
            break


def collatz_function(num):
    steps = 0
    global all_steps
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        steps += 1
    all_steps += steps


threads = []

it = iter(numbers)

for i in range(8):
    thread = threading.Thread(target=queue_process)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(all_steps / len(numbers))