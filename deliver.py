from datetime import timedelta

from load_trucks import (
    get_first_load,
    get_second_load,
    get_third_load,
    get_hash_table
)

from optimize_trucks import (
    address_lookup,
    get_current_distance,
    get_first_truck_indices,
    get_second_truck_indices,
    get_third_truck_indices,
    calc_shortest_distance,
)

hash_table = get_hash_table()

total_distance = 0

first_truck_departure_time = '08:00:00'
second_truck_departure_time = '09:10:00'
third_truck_departure_time = '11:00:00'

first_distance = 0
second_distance = 0
third_distance = 0

# Get sorted trucks from load_trucks.py and optimize them using our Greedy Algorithmm
first_truck = get_first_load()
calc_shortest_distance(first_truck, 1, 0)
optimized_first_truck = get_first_truck_indices()

second_truck = get_second_load()
calc_shortest_distance(second_truck, 2, 0)
optimized_second_truck = get_second_truck_indices()

third_truck = get_third_load()
calc_shortest_distance(third_truck, 3, 0)
optimized_third_truck = get_third_truck_indices()

# Convert timestamp string to time_delta
# Big O = O(1)
def convert_time_delta(time_stamp):
    (hrs, mins, secs) = time_stamp.split(':')
    return timedelta(
        hours=int(hrs), minutes=int(mins), seconds=int(secs))

# Convert distance traveled to time
# Big O = O(1)
def get_time(current_time, distance):
    distance_minutes = distance / 18
    new_time_string = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(distance_minutes * 60, 60)) + ':00'
    curr_delta = convert_time_delta(current_time)
    new_time_delta = convert_time_delta(new_time_string)
    return str(curr_delta + new_time_delta)

# Deliver packages to their destination
# Big O = O(n)
def deliver_packages(truck, distance, time):
    total_distance = 0
    prev_address = 0
    # Big O = O(n)
    for index, package in enumerate(truck):
        if index == len(truck):
            break
        else:
            package = hash_table.lookup(package)
            # Fix address for package #9
            if package.id == 9:
                package.set_address('410 S State St')
            address = address_lookup(package.address)
            distance = get_current_distance(prev_address, address)
            time = get_time(time, distance)
            package.set_status('Delivered')
            package.set_time_delivered(time)
            total_distance += distance
            prev_address = address

    return total_distance

# Send optimized truck loads out for delivery at their apropriate time
first_distance = deliver_packages(
    optimized_first_truck, first_distance, first_truck_departure_time)
second_distance = deliver_packages(
    optimized_second_truck, second_distance, second_truck_departure_time)
third_distance = deliver_packages(
    optimized_third_truck, third_distance, third_truck_departure_time)

total_distance = first_distance + second_distance + third_distance

# Get total distance traveled for all trucks
# Big O = O(1)
def get_total_distance():
    return total_distance
