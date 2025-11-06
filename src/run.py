from src.fan import generate_numbers, distribute_tasks
from src.worker import start_workers
from src.sink import collect_results

def main(numbers_count=100, worker_count=3):

    numbers = generate_numbers(numbers_count)

    task_queue, result_queue = distribute_tasks(numbers)

    processes = start_workers(worker_count, task_queue, result_queue)

    final_results = collect_results(result_queue, numbers_count, processes, task_queue)

    return final_results

if __name__ == "__main__":
    results = main()
    print(results)