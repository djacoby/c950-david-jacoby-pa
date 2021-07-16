import csv
from load_trucks import get_hash_table

hash_table = get_hash_table()

# Read distance & address csv files 
# Big O = O(1)
with open('./data/distances.csv', 'r', encoding='utf-8-sig') as distance_csv:
    distance_list = list(csv.reader(distance_csv))

with open('./data/addresses.csv', 'r', encoding='utf-8-sig') as address_csv:
    address_list = list(csv.reader(address_csv))

# Lookup address
# Big O = O(n)
def address_lookup(address):
    for entry in address_list:
        if entry[2] == address:
            return int(entry[0])

# Get total distance traveled
# Big O = O(1)
def get_total_distance(total, curr_index, dest_index):
    distance = distance_list[curr_index][dest_index]
    if distance == '':
        distance = [dest_index][curr_index]
    return total + float(distance)

# Get distance from current location to next location
# Big O = O(1)
def get_current_distance(curr_index, dest_index):
    distance = distance_list[curr_index][dest_index]
    if distance == '':
        distance = distance_list[dest_index][curr_index]
    return float(distance)


# Truck lists for packages
first_truck_indices = []

second_truck_indices = []

third_truck_indices = []

# Recursive function that caculates the shortest distance to the next delivery point using a "Greedy" Algorithm.
# The outer loop looks up every package in the hash table then checks if the distances to it is the closest distance
# from the current distance, if so it sets that is the new lowest_distance
#
# The inner loop then checks if the current package distance is equal to the lowest distance, if so it places it on the
# truck and pops that id from the list then sets the current_location to the location of the package that was placed on 
#
# the truck. Then it recursively calls calc_shortest_distance() with the shorten load list, truck number, and current location
# Big O = O(n^2)
def calc_shortest_distance(load, truck, curr_location):
    if len(load) == 0:
        return load
    else:
        try:
            lowest_distance = 50.0
            location = 0

            # Big O = O(n)
            for id in load:
                package = hash_table.lookup(id)
                next_location = address_lookup(package.address)

                if get_current_distance(curr_location, next_location) <= lowest_distance:
                    lowest_distance = get_current_distance(
                        curr_location, next_location)
                    location = next_location
            
            # Big O = O(n)
            for id in load:
                package = hash_table.lookup(id)
                next_location = address_lookup(package.address)

                if get_current_distance(curr_location, next_location) == lowest_distance:
                    if truck == 1:
                        first_truck_indices.append(package.id)
                        load.pop(load.index(id))
                        curr_location = location
                        calc_shortest_distance(load, 1, curr_location)

                    elif truck == 2:
                        second_truck_indices.append(package.id)
                        load.pop(load.index(id))
                        curr_location = location
                        calc_shortest_distance(load, 2, curr_location)

                    elif truck == 3:
                        third_truck_indices.append(package.id)
                        load.pop(load.index(id))
                        curr_location = location
                        calc_shortest_distance(load, 3, curr_location)
        except IndexError:
            pass

# Get filled hash table
# Big O = O(1)
def get_hash_table():
    return hash_table

# Get optimized first truck package indices
# Big O = O(1)
def get_first_truck_indices():
    return first_truck_indices

# Get optimized second truck package indices
# Big O = O(1)
def get_second_truck_indices():
    return second_truck_indices

# Get optimized third truck package indices
# Big O = O(1)
def get_third_truck_indices():
    return third_truck_indices
