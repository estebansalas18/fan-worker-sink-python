import multiprocessing as mp
import pytest
from src.fan import generate_numbers, distribute_tasks
from src.worker import start_workers
from src.sink import collect_results

# Tests: generate_numbers

def test_generate_numbers_count():
    nums = generate_numbers(10)
    assert len(nums) == 10

def test_generate_numbers_type():
    nums = generate_numbers(5)
    assert all(isinstance(n, int) for n in nums)
    
# Tests: collect_results positivo
def test_pipeline_small():
    numbers = [1, 2, 3, 4]
    excepted = [1, 4, 9, 16]

    task_queue, result_queue = distribute_tasks(numbers)
    processes = start_workers(2, task_queue, result_queue)
    result = collect_results(result_queue, len(numbers), processes, task_queue)

    assert result == excepted

def test_pipeline_random_correctness():
    numbers = generate_numbers(100)
    excepted = sorted(n * n for n in numbers)

    task_queue, result_queue = distribute_tasks(numbers)
    processes = start_workers(3, task_queue, result_queue)
    result = collect_results(result_queue, len(numbers), processes, task_queue)

    assert result == excepted

# Tests: collect_results negativo

def test_piepline_empty_input():
    numbers = []
    task_queue, result_queue = distribute_tasks(numbers)
    processes = start_workers(4, task_queue, result_queue)
    result = collect_results(result_queue, len(numbers), processes, task_queue)

    assert result == []

@pytest.mark.timeout(5)
def test_pipeline_large_volume():
    numbers = generate_numbers(1000)
    excepted = sorted(n * n for n in numbers)

    task_queue, result_queue = distribute_tasks(numbers)
    processes = start_workers(4, task_queue, result_queue)
    result = collect_results(result_queue, len(numbers), processes, task_queue)

    assert result == excepted