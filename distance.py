import csv

# Read disance & address csv files
with open('./data/distances.csv', 'r', encoding='utf-8-sig') as csv1:
    distance_list = list(csv.reader(csv1))

with open('./data/addresses.csv', 'r', encoding='utf-8-sig') as csv2:
    address_list = list(csv.reader(csv2))


def address_lookup(address):
    for entry in address_list:
        if entry[2] == address:
            return entry[0]
