import csv

def fix_shit(new_file):
    data_file = 'shit_happens/' + new_file
    print(data_file)

    with open(data_file) as f1, open(new_file, 'a') as f2:
        rows = csv.reader(f1)
        writer = csv.writer(f2)
        for row in rows:
            writer.writerow(row)
            print('done')

fix_shit('daily_active.csv')
fix_shit('daily_cases.csv')
fix_shit('daily_deaths.csv')