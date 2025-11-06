import sys
import pytest
import importlib


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


def test_cli_execution(monkeypatch, capfd):
    monkeypatch.setattr(sys, "argv", ["run.py", "5", "2"])

    # Mock main para evitar crear procesos reales
    def fake_main(n, w):
        return [1, 4, 9, 16, 25]
    
    monkeypatch.setattr("src.run.main", fake_main)

    import src.run
    importlib.reload(src.run)

    captured = capfd.readouterr()
    output = eval(captured.out.strip())  # convierte el texto impreso en lista

    assert output == [1, 4, 9, 16, 25]


def test_cli_invalid_args(monkeypatch, capfd):
    monkeypatch.setattr(sys, "argv", ["run.py", "abc", "xyz"])

    def fake_main(n, w):
        return [0]

    monkeypatch.setattr("src.run.main", fake_main)

    import src.run
    importlib.reload(src.run)

    captured = capfd.readouterr()
    output = eval(captured.out.strip())

    assert output == [0]
