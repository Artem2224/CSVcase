from main.main import BaseReader
import csv

def test_read_files(tmp_path):
    file = tmp_path / 'data.csv'
    file.write_text(
        "position,performance\n"
        "Backend,4.8\n"
        "Frontend,4.7\n"
    )

    reader = BaseReader()
    data = reader.read_files([file])

    assert len(data) == 2
    assert data[0]['position'] == 'Backend'
    assert data[1]['performance'] == '4.7'