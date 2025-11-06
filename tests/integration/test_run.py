from src.run import main

def test_main_with_parameters():
    result = main(numbers_count=10, worker_count=3)
    assert len(result) == 10
    assert all(isinstance(x, int) and x >= 0 for x in result)
    assert result == sorted(result)

def test_main_defaults():
    result = main()
    assert len(result) == 100
    assert all(isinstance(x, int) and x >= 0 for x in result)
    assert result == sorted(result)
