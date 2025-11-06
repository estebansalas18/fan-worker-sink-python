import pytest
from src.worker import worker, start_workers
import multiprocessing as mp

def test_worker_single_task():
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    task_queue.put(3)
    task_queue.put(None)  # stop signal

    p = mp.Process(target=worker, args=(task_queue, result_queue))
    p.start()
    p.join()

    assert result_queue.get() == 9
    assert result_queue.empty()

def test_start_workers_multiple_tasks():
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    numbers = [2,3,4]
    for n in numbers:
        task_queue.put(n)
    # stop signals
    worker_count = 2
    for _ in range(worker_count):
        task_queue.put(None)

    processes = start_workers(worker_count, task_queue, result_queue)
    for p in processes:
        p.join()

    results = sorted([result_queue.get() for _ in range(len(numbers))])
    assert results == [4,9,16]
