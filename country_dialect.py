import csv
input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='')as countries_data:
    # Instead of reading whole file to sniff we would read only 3 lines of the file to get the format and sniff
    sample = ""
    for line in range(3):
        sample += countries_data.readline()

    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    # Move the file pointer to the starting of the file
    countries_data.seek(0)
    # country_reader = csv.reader(countries_data, delimiter='|')
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace'
            ]

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")