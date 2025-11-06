import random
import multiprocessing as mp
import logging
import csv
from typing import List, Tuple

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s"
)
logger_fan = logging.getLogger("Fan")
logger_worker = logging.getLogger("Worker")
logger_sink = logging.getLogger("Sink")

# ------------------ Fan ------------------
def generate_numbers(count: int) -> List[int]:
    numbers = [random.randint(1, 100) for _ in range(count)]
    logger_fan.info(f"Generados {len(numbers)} números")
    return numbers

def distribute_tasks(numbers: List[int]) -> Tuple[mp.Queue, mp.Queue]:
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    for n in numbers:
        task_queue.put(n)
    return task_queue, result_queue

# ------------------ Worker ------------------
def worker(task_queue: mp.Queue, result_queue: mp.Queue, worker_id: int):
    logger_worker_local = logging.getLogger(f"Worker-{worker_id}")
    while True:
        n = task_queue.get()
        if n is None:
            break
        result = n * n
        logger_worker_local.info(f"procesó {n} → {result}")
        result_queue.put((worker_id, n, result))
    logger_worker_local.info("Finalizó")

def start_workers(worker_count: int, task_queue: mp.Queue, result_queue: mp.Queue) -> List[mp.Process]:
    processes = []
    for worker_id in range(1, worker_count + 1):
        p = mp.Process(target=worker, args=(task_queue, result_queue, worker_id))
        p.start()
        processes.append(p)
    return processes

# ------------------ Sink ------------------
def collect_results(result_queue: mp.Queue, expected_count: int, processes: List[mp.Process], task_queue: mp.Queue):
    # enviar señal de cierre
    for _ in processes:
        task_queue.put(None)

    processed_records = []

    for _ in range(expected_count):
        processed_records.append(result_queue.get())  # (worker_id, original, squared)

    for p in processes:
        p.join()

    logger_sink.info("Recolección completa")

    # exportar CSV
    with open("processing_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["worker_id", "original_value", "processed_value"])
        writer.writerows(processed_records)

    logger_sink.info("Archivo CSV generado: processing_log.csv ✅")

    # entregar solo los valores procesados (ordenados)
    return sorted(r[2] for r in processed_records)

# ------------------ Main Flow ------------------
def main(numbers_count: int = 100, worker_count: int = 3):
    numbers = generate_numbers(numbers_count)
    task_queue, result_queue = distribute_tasks(numbers)
    processes = start_workers(worker_count, task_queue, result_queue)
    final_results = collect_results(result_queue, numbers_count, processes, task_queue)
    return final_results

if __name__ == "__main__":
    results = main(1000, 3)
    print("Resultado final ordenado:", results)
