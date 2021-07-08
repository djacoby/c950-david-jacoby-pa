import csv

# Read disance & address csv files
with open('./data/distances.csv', 'r', encoding='utf-8-sig') as distance_csv:
    distance_list = list(csv.reader(distance_csv))

with open('./data/addresses.csv', 'r', encoding='utf-8-sig') as address_csv:
    address_list = list(csv.reader(address_csv))


def address_lookup(address):
    for entry in address_list:
        if entry[2] == address:
            return int(entry[0])


def get_total_distance(total, curr_index, dest_index):
    distance = distance_list[curr_index][dest_index]
    if distance == '':
        distance = [dest_index][curr_index]
    return total + float(distance)


def get_current_distance(curr_index, dest_index):
    distance = distance_list[curr_index][dest_index]
    if distance == '':
        distance = distance_list[dest_index][curr_index]
    return float(distance)


# Truck lists for packages
first_truck = []
second_truck = []
third_truck = []


def calc_shortest_distance(load, truck, curr_location):
    if len(load) == 0:
        return load
    else:
        try:
            lowest_distance = 50.0
            location = 0

            for package in load:
                next_location = address_lookup(package.address)

                if get_current_distance(location, next_location) <= lowest_distance:
                    lowest_distance = get_current_distance(
                        curr_location, next_location)
                    location = next_location

            for i in load:
                next_location = address_lookup(package.address)

                if get_current_distance(curr_location, next_location) == lowest_distance:
                    if truck == 1:
                        first_truck.append(i)
                        load.pop(load.index(i))
                        curr_location = location
                        calc_shortest_distance(load, truck, curr_location)

                    elif truck == 2:
                        second_truck.append(i)
                        load.pop(load.index(i))
                        curr_location = location
                        calc_shortest_distance(load, truck, curr_location)

                    elif truck == 3:
                        third_truck.append(i)
                        load.pop(load.index(i))
                        curr_location = location
                        calc_shortest_distance(load, truck, curr_location)
        except IndexError:
            pass


def get_first_truck():
    return first_truck


def get_second_truck():
    return second_truck


def get_third_truck():
    return third_truck
