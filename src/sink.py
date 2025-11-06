def collect_results(result_queue, expected_count, processes, task_queue):
    for _ in range(len(processes)):
        task_queue.put(None)

    results = []
    for _ in range(expected_count):
        results.append(result_queue.get())

    for p in processes:
        p.join()

    return sorted(results)