from hash_table import HashTable
from package import Package
import csv

from distance import get_first_truck, get_second_truck, calc_shortest_distance, get_third_truck
from load_trucks import get_first_load, get_second_load, get_third_load

first = get_first_load()
second = get_second_load()
third = get_third_load()

print(first)
print('')
print(second)
print('')
print(third)
print('')

calc_shortest_distance(first, 1, 0)
calc_shortest_distance(second, 2, 0)
calc_shortest_distance(third, 3, 0)

firstD = get_first_truck()
secondD = get_second_truck()
thirdD = get_third_truck()

print('')
print(firstD)
print(secondD)
print(thirdD)
print('')
