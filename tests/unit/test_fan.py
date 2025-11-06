import pytest
from src.fan import generate_numbers, distribute_tasks
import multiprocessing as mp

def test_generate_numbers_count():
    nums = generate_numbers(10)
    assert len(nums) == 10

def test_generate_numbers_type():
    nums = generate_numbers(5)
    assert all(isinstance(n, int) for n in nums)

def test_distribute_tasks_queues():
    numbers = [1,2,3]
    task_queue, result_queue = distribute_tasks(numbers)

    items = [task_queue.get() for _ in range(len(numbers))]
    
    assert sorted(items) == [1,2,3]
    assert result_queue.empty()