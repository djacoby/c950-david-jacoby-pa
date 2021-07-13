import datetime

from optimize_trucks import get_hash_table, get_all_truck_indices
from deliver import get_total_distance, convert_time_delta

total_distance = get_total_distance()
hash_table = get_hash_table()
all_truck_indices = get_all_truck_indices()

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

user_input = input("""
Please select an option below:
  0. Exit
  1. Get the info for all packages at a particular time.
  2. Get the info for a specific package at a particular time.
""")

while user_input != '0':
    if user_input == '1':
        input_time = input("Enter a time (HH:MM:SS) ")
        user_time_delta = convert_time_delta(input_time)
        for index, id in enumerate(all_truck_indices):
            package = hash_table.lookup(id)
            time_delivered = package.get_time_delivered()
            delivered_delta = convert_time_delta(time_delivered)
            if delivered_delta.seconds > user_time_delta.seconds:
                package.set_time_delivered(None)
                package.set_status('Not Delivered')
            package.to_string()
