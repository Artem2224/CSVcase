import csv
import argparse
from tabulate import tabulate

class BaseReader:
    def __init__(self):
        self.reader = []
        self.result = []
        self.extraction = None


    def read_files(self, paths):
        for path in paths:
            with open(path, 'r') as file:
                reader_csv = csv.DictReader(file)
                self.reader.extend(list(reader_csv))
        return self.reader

    def extract_data(self, *list_data):
        self.result = []
        for row in self.reader:
            data_dict = {}
            for data in list_data:
                try:
                    data_dict[data] = float(row[data])
                except ValueError:
                    data_dict[data] = row[data]
            self.result.append(data_dict)
        return self.result
    
    def create_report(self, report):
        with open(f'{report}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.result[0].keys())
            if isinstance(self.extraction, dict) and self.extraction:
                for key, value in self.extraction.items():
                    writer.writerow([key, value])
            else:
                for row in self.result:
                    writer.writerow(list(row.values()))
                 
    def create_tabulate(self):
        print(tabulate(self.result, headers='keys'))
class AvgPerformance(BaseReader):

    def extract_data(self, *list_data):
        super().extract_data(*list_data)
        self.extraction = {}
        for row in self.result:
            position = row['position']
            performance = float(row['performance'])
            if position not in self.extraction:
                 self.extraction[position] = {
                        'performance_sum': performance,
                        'count': 1
                    }
            else:
                self.extraction[position]['performance_sum'] += performance
                self.extraction[position]['count'] += 1
        for key in self.extraction:
            self.extraction[key] = round(self.extraction[key]['performance_sum']/self.extraction[key]['count'], 2)
        self.extraction = dict(sorted(self.extraction.items(), key=lambda item: item[1], reverse=True))

    def create_tabulate(self):
        tablet = list(zip(self.extraction.keys(), self.extraction.values()))
        index = range(1, len(self.extraction) + 1)
        print(tabulate(tablet, headers=['position', 'performance'], showindex=index))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+')
    parser.add_argument('--report', nargs='?', const='performance', default='performance')

    args = parser.parse_args()
    base = AvgPerformance()
    base.read_files(args.files)
    base.extract_data('position', 'performance')
    base.create_report(args.report)
    base.create_tabulate()


if __name__ == '__main__':
    main()