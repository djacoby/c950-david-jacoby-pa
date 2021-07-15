import csv

from hash_table import HashTable
from package import Package

hash_table = HashTable()

package_indices = []
first_truck = []
second_truck = []
third_truck = []

# Load trucks based off special instructions/ deadline
# Big 0 = 0(n)
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

        package_indices.append(id)
        hash_table.insert(id, package)

        if '84104' in zip and '10:30' not in deadline:
            third_truck.append(package.id)

        if deadline != 'EOD':
            if 'Must' in special_instructions or 'None' in special_instructions:
                first_truck.append(package.id)
                continue

        if 'Can' in special_instructions or 'Delayed' in special_instructions:
            second_truck.append(package.id)
            continue

        if 'Must' in special_instructions:
            first_truck.append(package.id)
            continue

        if package.id not in first_truck and package.id not in second_truck and package.id not in third_truck:
            if len(second_truck) > len(third_truck):
                third_truck.append(package.id)
            else:
                second_truck.append(package.id)

# Return loaded hash table
# Big 0 = 0(1)
def get_hash_table():
    return hash_table

# Return first load
# Big 0 = 0(1)
def get_first_load():
    return first_truck

# Return second load
# Big 0 = 0(1)
def get_second_load():
    return second_truck

# Return third load
# Big 0 = 0(1)
def get_third_load():
    return third_truck

# Return all package indices
# Big 0 = 0(1)
def get_package_indices():
    return package_indices
