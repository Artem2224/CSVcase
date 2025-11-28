from main.main import BaseReader

def test_extract_data():
    reader = BaseReader()
    reader.reader = [
        {"position": "Backend", "performance": "4.8"},
        {"position": "Frontend", "performance": "4.7"},
    ]

    result = reader.extract_data("position", "performance")

    assert result[0]["performance"] == 4.8
    assert result[1]["position"] == "Frontend"