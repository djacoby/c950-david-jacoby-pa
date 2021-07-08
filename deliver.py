from load_trucks import (
    get_first_load,
    get_second_load,
    get_third_load,
    get_hash_table
)

from optimize_trucks import (
    address_lookup,
    get_current_distance,
    get_first_truck,
    get_first_truck_indices,
    get_second_truck,
    get_second_truck_indices,
    get_third_truck,
    get_third_truck_indices,
    calc_shortest_distance,
)

hash_table = get_hash_table()

total_distance = 0

first_truck_departure_time = '08:00:00'
second_truck_departure_time = '09:10:00'
third_truck_departure_time = '11:00:00'

# TODO: get_time function

first_truck = get_first_load()
calc_shortest_distance(first_truck, 1, 0)
optimized_first_truck = get_first_truck_indices()

second_truck = get_second_load()
calc_shortest_distance(second_truck, 2, 0)
optimized_second_truck = get_second_truck_indices()

third_truck = get_first_load()
calc_shortest_distance(third_truck, 3, 0)
optimized_third_truck = get_third_truck_indices()

# prev_address = 0

# for index, package in enumerate(optimized_first_truck):
#     if index == len(optimized_first_truck):
#         break
#     else:
#         package = hash_table.lookup(package)
#         address = address_lookup(package.address)
#         total_distance += get_current_distance(prev_address, address)
#         prev_address = address


def deliver_packages(truck):
    distance = 0
    prev_address = 0
    for index, package in enumerate(truck):
        if index == len(truck):
            break
        else:
            package = hash_table.lookup(package)
            address = address_lookup(package.address)
            distance += get_current_distance(prev_address, address)
            prev_address = address

    return distance


first_truck_distance = deliver_packages(optimized_first_truck)
second_truck_distance = deliver_packages(optimized_second_truck)
third_truck_distance = deliver_packages(optimized_third_truck)

total_distance = first_truck_distance + \
    second_truck_distance + third_truck_distance

print(total_distance)
