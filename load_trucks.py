import csv

from hash_table import HashTable
from package import Package

hash_table = HashTable()

MAX_CAPACITY = 16

first_truck = []
second_truck = []
third_truck = []

with open('./data/packages.csv', 'r', encoding='utf-8-sig') as csv_file:
    package_reader = csv.reader(csv_file)
    for row in package_reader:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        special_instructions = row[7]

        package = Package(id, address, city, state, zip,
                          deadline, weight, special_instructions)

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

        hash_table.insert(id, package)


def get_hash_table():
    return hash_table


def get_first_truck():
    return first_truck


def get_second_truck():
    return second_truck


def get_third_truck():
    return third_truck


# first = get_first_truck()
# second = get_second_truck()
# third = get_third_truck()

# print(len(first))
# print(first)
# print(len(second))
# print(second)
# print(len(third))
# print(third)
