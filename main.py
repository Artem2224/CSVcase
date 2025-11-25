import csv


def calc(*paths):
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
    
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file,)
        writer.writerow(['position', 'performance'])
        for pos, perf in result.items():
            writer.writerow([pos, perf])


a = calc('employees1.csv', 'employees2.csv')