import csv
import argparse

def calc(paths, report):
    result = {}
    for path in paths:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                position = row['position']
                performance = float(row['performance'])
                if position not in result:
                    result[position] = {
                        'performance_sum': performance,
                        'count': 1
                    }
                else:
                    result[position]['performance_sum'] += performance
                    result[position]['count'] += 1
    for key in result:
        result[key] = round(result[key]['performance_sum']/result[key]['count'], 2)
    with open(f'{report}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['position', 'performance'])
        for pos, perf in result.items():
            writer.writerow([pos, perf])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+')
    parser.add_argument('--report', nargs='?', const='performance', default='performance')

    args = parser.parse_args()
    calc(args.files, args.report)

if __name__ == '__main__':
    main()