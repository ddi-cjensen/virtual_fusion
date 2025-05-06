import csv
import json

filedata = []
split_data = []

try:
    with open('io_card_def.csv', 'r') as inpoop_file:
        csv_reader = csv.reader(inpoop_file)
        filedata = list(csv_reader)
except Exception as e:
    print(e)

for row in filedata:
    split_data.append(row[0].split(','))

output_stage = {}

for row in split_data:
    print(row)
    output_stage[row[1].strip().replace('"','')] = {
        "io_type": row[5].strip().replace('"',''),
        "desc": row[2].strip().replace('"','')
    }

with open('io_card_def.json', 'w') as output_json:
    json.dump(output_stage, output_json, indent=2)

