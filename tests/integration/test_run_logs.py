# test_processing.py
import os
import pytest
import multiprocessing as mp
from src import run_logs  # o como tengas tu archivo principal

# ------------------ Fan ------------------
def test_generate_numbers_length():
    numbers = run_logs.generate_numbers(50)
    assert len(numbers) == 50
    assert all(1 <= n <= 100 for n in numbers)

def test_distribute_tasks_content():
    numbers = [1, 2, 3]
    task_queue, result_queue = run_logs.distribute_tasks(numbers)
    retrieved = [task_queue.get() for _ in range(len(numbers))]
    assert retrieved == numbers
    # result_queue debe estar vacío inicialmente
    assert result_queue.empty()

# ------------------ Worker ------------------
def test_worker_puts_results():
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    numbers = [2, 3]
    for n in numbers:
        task_queue.put(n)
    task_queue.put(None)  # señal de cierre

    p = mp.Process(target=run_logs.worker, args=(task_queue, result_queue, 1))
    p.start()
    p.join()

    results = [result_queue.get() for _ in range(len(numbers))]
    worker_ids, original_vals, squared_vals = zip(*results)
    assert squared_vals == tuple([n*n for n in numbers])
    assert all(wid == 1 for wid in worker_ids)

# ------------------ Sink ------------------
def test_collect_results_creates_csv(tmp_path):
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    numbers = [2, 4]
    for n in numbers:
        task_queue.put(n)
    # lanzar workers
    processes = run_logs.start_workers(1, task_queue, result_queue)
    final_results = run_logs.collect_results(result_queue, len(numbers), processes, task_queue)
    
    # verificar resultados
    assert final_results == sorted([n*n for n in numbers])
    # verificar CSV
    assert os.path.exists("processing_log.csv")
    with open("processing_log.csv") as f:
        content = f.read()
    assert "worker_id,original_value,processed_value" in content

    # limpiar CSV
    os.remove("processing_log.csv")

# ------------------ Main ------------------
def test_main_with_parameters():
    result = run_logs.main(numbers_count=10, worker_count=3)
    assert len(result) == 10
    assert result == sorted(result)

def test_main_defaults():
    result = run_logs.main()
    assert len(result) == 100
    assert result == sorted(result)
