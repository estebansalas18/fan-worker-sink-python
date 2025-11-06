from src.run import main

def test_run_main():
    result = main(numbers_count=10, worker_count=3)
    # debe tener 10 elementos, todos positivos
    assert len(result) == 10
    assert all(isinstance(x, int) and x >= 0 for x in result)
    # debe estar ordenado ascendente
    assert result == sorted(result)
