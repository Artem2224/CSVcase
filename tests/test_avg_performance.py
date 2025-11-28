from main.main import AvgPerformance

def test_avg_performance():
    perf = AvgPerformance()
    perf.reader = [
        {"position": "Backend", "performance": "4.8"},
        {"position": "Backend", "performance": "5.0"},
        {"position": "Frontend", "performance": "4.7"},
    ]

    perf.extract_data("position", "performance")

    assert perf.extraction["Backend"] == 4.9
    assert perf.extraction["Frontend"] == 4.7

    keys = list(perf.extraction.keys())
    assert keys == ["Backend", "Frontend"]