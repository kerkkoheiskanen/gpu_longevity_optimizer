import csv
import math

csv_name = "gpu_stats_112022.csv"

gpu_data = []

with open(csv_name) as csvfile:
    reader = csv.DictReader(csvfile)
    keys = reader.fieldnames

    for row in reader:
        data = {}
        for key in keys:
            data[key] = row[key]

        gpu_data.append(data)

gpu_performances = {}

for gpu in gpu_data:
    name = gpu["Graphics Card"]
    perf = float(gpu["4K Ultra perf"].strip('%'))

    # Yearly relative computing power depreciation constant. This should probably be in the range of 0.001 to 0.05
    r = 0.223

    # Computing power limit the user wants their current gpu to be above of
    # compared to the current best gpu (where current best = 100)
    perf_limit = 27.3

    # Calculate the amount of months it takes for the relative computing power to 
    # drop below the performance limit
    years = (perf - perf_limit)/(perf * r)

    gpu_performances[name] = years/int(gpu["Price"])*100

sorted_perf = {k: v for k, v in sorted(gpu_performances.items(), key=lambda item: item[1])}
for k,v in sorted_perf.items():
    print(k + " has " + str(round(v,3)) + " years of acceptable gaming per hundred euros" )
