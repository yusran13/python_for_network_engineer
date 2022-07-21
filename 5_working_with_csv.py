import csv, json
import pandas as pd
from pprint import pprint

#CARA 1
# with open('All Devices Jul 21, 2022 10.41.30 AM.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         print(f"{row['Device Name']} - {row['IP Address']} - {row['Device Type']} - {row['Location']}")
#         line_count += 1
#     print(f'Processed {line_count} lines.')

#CARA 2 --> PANDAS
# df = pd.read_csv('All Devices Jul 21, 2022 10.41.30 AM.csv')
# data_json = json.loads(df.to_json(orient="records"))

# print("Finish loading data")
# print("--------------------------------------------")
# pprint(data_json)
# print("Total Rows", len(data_json))

# print("--------------------------------------------")