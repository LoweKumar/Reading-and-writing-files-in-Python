import json
import urllib.request

# ************* Reading data from file ************************
# json_data_source = 'temperature_anomaly.json'
# with open(json_data_source, encoding='utf-8') as data:
# anomalies = json.load(data)
#

# ****** Reading data from url rather than a file ************
json_data_source = 'https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)



# print(anomalies['description'])

for keys, values in anomalies['description'].items():
    print(f"{keys} : {values}")

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)

