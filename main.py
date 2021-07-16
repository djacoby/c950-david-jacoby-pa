# David Jacoby Student ID: #000306735

from optimize_trucks import get_hash_table
from deliver import get_total_distance, convert_time_delta
from load_trucks import get_package_indices

total_distance = get_total_distance()
hash_table = get_hash_table()
all_truck_indices = get_package_indices()

# Dashes for header section of package info table
dash = '-' * 40

# Prompt user for a time and convert to time_delta
# Big O = O(1)
def get_user_time_input():
    input_time = input("Enter a time (HH:MM:SS): ")
    user_time_delta = convert_time_delta(input_time)
    return user_time_delta

# Print table header for package status info
# Big O = O(1)
def print_table_header():
    print(dash)
    print('ID         DEADLINE          STATUS')
    print(dash)

# Print package status info
# Big O = O(1)
def print_package_info(id, user_time_delta):
    package = hash_table.lookup(id)
    time_delivered = package.get_time_delivered()
    delivered_delta = convert_time_delta(time_delivered)
    status = f'ID: {package.id}{" " if package.id <= 9 else ""}  Deadline: {package.deadline}{"     " if package.deadline == "EOD" else ""} Status: Delivered at {package.time_delivered}'
    if delivered_delta.seconds > user_time_delta.seconds:
        status = f'ID: {package.id}{" " if package.id <= 9 else ""}  Deadline: {package.deadline}{"     " if package.deadline == "EOD" else ""} Status: Not Delivered'
    print(status)

# Prompt user for info selection (single package/ all packages)
# Big O = O(1)
def prompt_user():
    return input("""
  Please select an option below:
    1. Get the info for all packages at a particular time.
    2. Get the info for a specific package at a particular time.
    (Enter any other key to exit at any time)
  """)


print("""\
 __          _______ _    _ _____  _    _  _____    _____    ____  _    _ _______ _____ _   _  _____
 \ \        / / ____| |  | |  __ \| |  | |/ ____|  |  __ \  / __ \| |  | |__   __|_   _| \ | |/ ____|
  \ \  /\  / / |  __| |  | | |__) | |  | | (___    | |__) || |  | | |  | |  | |    | | |  \| | |  __
   \ \/  \/ /| | |_ | |  | |  ___/| |  | |\___ \   |  _  / | |  | | |  | |  | |    | | | . ` | | |_ |
    \  /\  / | |__| | |__| | |    | |__| |____) |  | | \ \ | |__| | |__| |  | |   _| |_| |\  | |__| |
     \/  \/   \_____|\____/|_|    \____/ |_____/   |_|  \_\ \____/ \____/   |_|  |_____|_| \_|\_____|

                         _____  _____    ____   _____ _____            __  __
                        |  __ \|  __ \  / __ \ / ____|  __ \     /\   |  \/  |
                        | |__) | |__) || |  | | |  __| |__) |   /  \  | \  / |
                        |  ___/|  _  / | |  | | | |_ |  _  /   / /\ \ | |\/| |
                        | |    | | \ \ | |__| | |__| | | \ \  / ____ \| |  | |
                        |_|    |_|  \_\ \____/ \_____|_|  \_\/_/    \_\_|  |_|
  """)

print(f'\nThe route was completeted in {total_distance:.2f} miles\n')

user_input = prompt_user()

# Driver for program
# Big O = O(n)
while user_input != '0':
    try:
        # Get all package info for a specific time
        if user_input == '1':
            user_time_delta = get_user_time_input()
            for index, id in enumerate(all_truck_indices):
                print_package_info(id, user_time_delta)
        # Get infor for a specific package at a specific time
        elif user_input == '2':
            package_id = input("Enter a package id: ")
            user_time_delta = get_user_time_input()
            print_package_info(int(package_id), user_time_delta)
        else:
            print("Invalid input, exiting now...")
            exit()
    except ValueError:
        print('Invalid input, exiting now...')
        exit()
