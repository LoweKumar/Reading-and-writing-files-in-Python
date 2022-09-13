import csv

input_filename = 'country_info.txt'
countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # country_file.readline()
    dict_reader = csv.DictReader(country_file, delimiter='|')
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['Country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['CC'].casefold()] = row


print(countries)
while True:
    country_name = input("Enter the country name: ").casefold()
    if country_name in countries:
        country_data = countries[country_name]
        print(f"The country {country_name} capital is {country_data['capital']}")
    elif country_name == 'quit':
        break





