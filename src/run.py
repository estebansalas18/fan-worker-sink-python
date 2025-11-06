from src.fan import generate_numbers, distribute_tasks
from src.worker import start_workers
from src.sink import collect_results
import sys

def main(numbers_count=100, worker_count=3):

    numbers = generate_numbers(numbers_count)

    task_queue, result_queue = distribute_tasks(numbers)

    processes = start_workers(worker_count, task_queue, result_queue)

    final_results = collect_results(result_queue, numbers_count, processes, task_queue)

    return final_results

if __name__ == "__main__":
    # Leer argumentos desde consola (opcionales)
    # Ejemplo:
    #   python run.py 200 5
    # Si no pasan nada → toma los valores por defecto
    
    if len(sys.argv) >= 2:
        try:
            numbers_count = int(sys.argv[1])
        except ValueError:
            numbers_count = 100
    else:
        numbers_count = 100

    if len(sys.argv) >= 3:
        try:
            worker_count = int(sys.argv[2])
        except ValueError:
            worker_count = 3
    else:
        worker_count = 3

    results = main(numbers_count, worker_count)
    print(results)