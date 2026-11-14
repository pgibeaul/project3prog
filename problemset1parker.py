# setting constant variables for days, hours and creating a divider to match sample output
days = 5
minimum_hours = 7
maximum_hours = 24
divider = "-" * 70

# creating a function that takes users input for their work hours and validates it
def get_valid_hours(day_number):
    while True:
        hours = input(f"Enter hours worked on Day #{day_number}: ").strip()
        if not hours.isdigit():
            print("Please enter a whole number.")
        elif int(hours) > maximum_hours:
            print(f"Hours must be between 0 and {maximum_hours}.")
        else:
            return int(hours)

# creating a function that collects hours worked for each day and returns them as a list
def get_all_hours(days):
    hour_list = []
    for day_number in range(1, days + 1):
        hour_list.append(get_valid_hours(day_number))
    return hour_list

# creating a function that finds the highest hours worked and returns every day number that matched it
def highest_days(hour_list):
    highest = max(hour_list)
    high_days = []
    day_number = 1
    for hours in hour_list:
        if hours == highest:
            high_days.append(day_number)
        day_number += 1
    return highest, high_days
