import pytest
from src.sink import collect_results
import multiprocessing as mp

def test_sink_collect_sorted():
    result_queue = mp.Queue()
    numbers = [3,1,2]
    for n in numbers:
        result_queue.put(n)
    # no processes or task_queue needed for simple test
    final = collect_results(result_queue, len(numbers), [], mp.Queue())
    assert final == [1,2,3]

def test_sink_empty_queue():
    result_queue = mp.Queue()
    final = collect_results(result_queue, 0, [], mp.Queue())
    assert final == []
