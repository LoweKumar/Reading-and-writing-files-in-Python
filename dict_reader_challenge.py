import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # get the column heading from first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    # country_file.readline()
    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row


print(countries)
while True:
    country_name = input("Enter the country name: ").casefold()
    if country_name in countries:
        country_data = countries[country_name]
        print(f"The country {country_name} capital is {country_data['capital']}")
    elif country_name == 'quit':
        break





