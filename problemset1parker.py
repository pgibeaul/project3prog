# setting constant variables for days, hours and creating a divider
days = 5
minimum_hours = 7
maximum_hours = 24
divider = "-" * 70

# creating functions and their logic
def get_valid_hours(day_number):
    while True:
        hours = input(f"Enter hours worked on Day #{day_number}: ").strip()
        if not hours.isdigit():
            print("Please enter a whole number.")