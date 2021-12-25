import csv
import jsonlines

file_name = "./test.jl"
csv_file_name = "./test.csv"

csv_data = open(csv_file_name, 'w+')
csv_writer = csv.writer(csv_data)

count = 0
with jsonlines.open(file_name) as reader:
    for obj in reader:
        if count == 0:
            csv_writer.writerow(obj.keys())
            count += 1
        csv_writer.writerow(obj.values())
