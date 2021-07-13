from datetime import datetime, date

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

first_distance = 0
second_distance = 0
third_distance = 0

first_truck = get_first_load()
calc_shortest_distance(first_truck, 1, 0)
optimized_first_truck = get_first_truck_indices()

second_truck = get_second_load()
calc_shortest_distance(second_truck, 2, 0)
optimized_second_truck = get_second_truck_indices()

third_truck = get_third_load()
calc_shortest_distance(third_truck, 3, 0)
optimized_third_truck = get_third_truck_indices()


def get_time(current_time, distance):
    parsed_time = datetime.strptime(current_time, "%H:%M:%S")
    distance_minutes = distance / 18
    new_time_string = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(distance_minutes * 60, 60)) + ':00'
    parsed_new_time = datetime.strptime(
        new_time_string, "%H:%M:%S")
    new_hours = parsed_time.hour + parsed_new_time.hour
    new_minutes = parsed_time.minute + parsed_new_time.minute
    if new_minutes > 59:
        new_minutes = new_minutes - 60
        new_hours += 1
    new_seconds = parsed_time.second + parsed_new_time.second
    new_time = datetime(date.today().year, date.today().month,
                        date.today().day, new_hours, new_minutes, new_seconds)
    return new_time.strftime("%H:%M:%S")


def deliver_packages(truck, distance, time):
    total_distance = 0
    prev_address = 0
    for index, package in enumerate(truck):
        if index == len(truck):
            break
        else:
            package = hash_table.lookup(package)
            address = address_lookup(package.address)
            distance = get_current_distance(prev_address, address)
            time = get_time(time, distance)
            package.set_status('Delivered')
            package.set_time_delivered(time)
            print(package.time_delivered)
            total_distance += distance
            prev_address = address

    return total_distance


first_distance = deliver_packages(
    optimized_first_truck, first_distance, first_truck_departure_time)
second_distance = deliver_packages(
    optimized_second_truck, second_distance, second_truck_departure_time)
third_distance = deliver_packages(
    optimized_third_truck, third_distance, third_truck_departure_time)

total_distance = first_distance + second_distance + third_distance

print(total_distance)
