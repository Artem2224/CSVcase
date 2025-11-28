from main.main import AvgPerformance

def test_create_report(tmp_path):
    perf = AvgPerformance()
    perf.extraction = {
        "Backend": 4.9,
        "Frontend": 4.7
    }

    report_path = tmp_path / "out"
    perf.result = [{"position": "x", "performance": 1}]

    perf.create_report(report_path)

    content = (tmp_path / "out.csv").read_text()

    assert "Backend" in content
    assert "4.9" in content
    assert "Frontend" in content