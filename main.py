from load_trucks import get_first_load, get_second_load, get_third_load, get_hash_table
from hash_table import HashTable
from package import Package
import csv

from optimize_trucks import (
    get_first_truck,
    get_first_truck_indices,
    get_second_truck,
    get_second_truck_indices,
    get_third_truck,
    get_third_truck_indices,
    calc_shortest_distance
)


first = get_first_load()
# second = get_second_load()
# third = get_third_load()

for package in first:
    print(package)

print('-----------------------------------')

# for package in second:
#     print(package.id)

# print('-----------------------------------')

# for package in third:
#     print(package.id)

# print('-----------------------------------')

calc_shortest_distance(first, 1, 0)
# calc_shortest_distance(second, 2, 0)
# calc_shortest_distance(third, 3, 0)

firstD = get_first_truck_indices()
# secondD = get_second_truck_indices()
# thirdD = get_third_truck_indices()

for package in firstD:
    print(package)

print('-----------------------------------')

# for package in secondD:
#     print(package)

# print('-----------------------------------')

# for package in thirdD:
#     print(package)
