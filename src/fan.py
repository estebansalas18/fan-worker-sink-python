import random
import multiprocessing as mp

def generate_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def distribute_tasks(numbers):
    task_queue = mp.Queue()
    result_queue = mp.Queue()

    for n in numbers:
        task_queue.put(n)

    return task_queue, result_queue