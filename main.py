import json


with open('countries.json', encoding='utf-8') as database:
    countries = json.load(database)
    country = input('Введите страну: ')
    for key in countries[country]:
        print(f'{key} - {countries[country][key]}')


