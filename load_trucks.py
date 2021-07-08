import csv

from hash_table import HashTable
from package import Package

hash_table = HashTable()

first_truck = []
second_truck = []
third_truck = []

with open('./data/packages.csv', 'r', encoding='utf-8-sig') as csv_file:
    package_reader = csv.reader(csv_file)
    for row in package_reader:
        id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        special_instructions = row[7]

        package = Package(id, address, city, state, zip,
                          deadline, weight, special_instructions)

        hash_table.insert(id, package)

        if deadline != 'EOD':
            if 'Must' in special_instructions or 'None' in special_instructions:
                first_truck.append(package.id)
                continue

        if 'Can' in special_instructions:
            second_truck.append(package.id)
            continue

        if 'Delayed' in special_instructions:
            second_truck.append(package.id)
            continue

        if 'Wrong' in special_instructions:
            third_truck.append(package.id)
            continue

        if 'Must' in special_instructions:
            first_truck.append(package.id)
            continue

        if package.id not in first_truck and package.id not in second_truck and package.id not in third_truck:
            if len(second_truck) > len(third_truck):
                third_truck.append(package.id)
            else:
                second_truck.append(package.id)


def get_hash_table():
    return hash_table


def get_first_load():
    return first_truck


def get_second_load():
    return second_truck


def get_third_load():
    return third_truck
