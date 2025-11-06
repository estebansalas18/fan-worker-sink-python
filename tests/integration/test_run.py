import pytest
from unittest.mock import patch, MagicMock
from src.run import main


def test_main_with_defaults():
    # Mock de funciones importadas en run.py
    with patch("src.run.generate_numbers") as mock_generate, \
         patch("src.run.distribute_tasks") as mock_distribute, \
         patch("src.run.start_workers") as mock_start_workers, \
         patch("src.run.collect_results") as mock_collect:

        # Valores mockeados
        mock_generate.return_value = [1, 2, 3]
        mock_distribute.return_value = ("task_queue", "result_queue")
        mock_start_workers.return_value = ["p1", "p2"]
        mock_collect.return_value = [1, 2, 3]

        result = main()  # usa valores default: 100 y 3

        mock_generate.assert_called_once_with(100)
        mock_distribute.assert_called_once_with([1, 2, 3])
        mock_start_workers.assert_called_once_with(3, "task_queue", "result_queue")
        mock_collect.assert_called_once_with("result_queue", 100, ["p1", "p2"], "task_queue")

        assert result == [1, 2, 3]


def test_main_with_parameters():
    with patch("src.run.generate_numbers") as mock_generate, \
         patch("src.run.distribute_tasks") as mock_distribute, \
         patch("src.run.start_workers") as mock_start_workers, \
         patch("src.run.collect_results") as mock_collect:

        mock_generate.return_value = list(range(5))
        mock_distribute.return_value = ("q1", "q2")
        mock_start_workers.return_value = ["p1"]
        mock_collect.return_value = [0, 1, 2, 3, 4]

        result = main(5, 1)

        mock_generate.assert_called_once_with(5)
        mock_distribute.assert_called_once_with(list(range(5)))
        mock_start_workers.assert_called_once_with(1, "q1", "q2")
        mock_collect.assert_called_once_with("q2", 5, ["p1"], "q1")

        assert result == [0, 1, 2, 3, 4]
        assert len(result) == 5
