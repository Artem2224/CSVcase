from main.main import AvgPerformance
from unittest.mock import patch

def test_tabulate_output():
    perf = AvgPerformance()
    perf.extraction = {"Backend": 4.9, "Frontend": 4.7}

    with patch("builtins.print") as mock_print:
        perf.create_tabulate()

    mock_print.assert_called()