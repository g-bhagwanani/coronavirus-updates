from aux_functions import get_details_of, list_of_countries
import datetime
import csv
import os

date = datetime.datetime.now().strftime("%d %b")
total_cases = [date]
active_cases = [date]
total_deaths = [date]

for country in list_of_countries:
    try:
        if country == 'World':
            country = 'total:'
        info = get_details_of(country)
        total_cases.append(info[0])
        active_cases.append(info[5])
        total_deaths.append(info[2])
    except Exception as e:
        print(country)
        print(e)

abs_file_path = os.path.abspath(__file__)
abs_directory_path = abs_file_path.replace(abs_file_path.split('/')[-1], '')
print(abs_directory_path)

with open(abs_directory_path + 'daily_cases.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(total_cases)

with open(abs_directory_path + 'daily_active.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(active_cases)

with open(abs_directory_path + 'daily_deaths.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(total_deaths)