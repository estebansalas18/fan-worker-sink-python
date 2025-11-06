from src.run import main
import subprocess
import sys

def test_run_main_with_explicit_values():
    result = main(numbers_count=10, worker_count=3)

    assert len(result) == 10

    assert all(isinstance(x, int) and x >= 0 for x in result)

    assert result == sorted(result)

def test_run_cli_defaults():
    result = subprocess.check_output([sys.executable, "src/run.py"])
    output = result.decode().strip()

    numbers = list(map(int, output.strip("[]").split(",")))

    assert len(numbers) == 100

    assert numbers == sorted(numbers)
