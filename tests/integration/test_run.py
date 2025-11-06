import pytest

def test_main_with_parameters():
    from src.run import main
    result = main(numbers_count=10, worker_count=3)
    assert len(result) == 10
    assert result == sorted(result)


def test_main_defaults():
    from src.run import main
    result = main()
    assert len(result) == 100
    assert result == sorted(result)