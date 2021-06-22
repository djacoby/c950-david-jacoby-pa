import csv
from load_trucks import get_hash_table, get_first_truck, get_second_truck, get_third_truck

# Read disance & address csv files
with open('./data/distances.csv', 'r', encoding='utf-8-sig') as distance_csv:
    distance_list = list(csv.reader(distance_csv))

with open('./data/addresses.csv', 'r', encoding='utf-8-sig') as address_csv:
    address_list = list(csv.reader(address_csv))


def address_lookup(address):
    for entry in address_list:
        if entry[2] == address:
            return entry[0]


def get_distance(curr_index, dest_index):
    return address_list[curr_index][dest_index]


# Truck lists for packages
first_truck = []
second_truck = []
third_truck = []
