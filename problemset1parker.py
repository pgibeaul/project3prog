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