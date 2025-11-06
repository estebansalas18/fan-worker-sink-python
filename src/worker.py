import multiprocessing as mp

def worker(task_queue, result_queue):
    while True:
        n = task_queue.get()
        if n is None:
            break
        result_queue.put(n * n)

def start_workers(worker_count, task_queue, result_queue):
    processes = []
    for _ in range(worker_count):
        p = mp.Process(target=worker, args=(task_queue, result_queue))
        p.start()
        processes.append(p)
    return processes