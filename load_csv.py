import csv
import matplotlib.pyplot as plt

with open('weather_file.csv', newline='') as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader]

temp_list = []
pressure_list = []
date_list = []

for row in rows:
    if row['key'] == 'temp':
        temp_list.append(row['value'])
    if row['key'] == 'pressure':
        pressure_list.append(row['value'])
    if row['key'] == 'date':
        date_list.append(row['value'])

print(temp_list)
print(pressure_list)
print(date_list)

plt.plot(date_list, temp_list)
plt.show()