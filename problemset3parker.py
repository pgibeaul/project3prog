# creating first function that asks for a whole number and prompts them to try again if the number they entered was too low
def get_number(prompt, minimum):
    while True:
        text = input(prompt).strip()
        if not text.isdigit():
            print("Enter a whole number.")
        elif int(text) < minimum:
            print(f"Enter a number of at least {minimum}.")
        else:
            return int(text)

# creating a function that asks for a guides name and prompts an error message if entered incorrectly
def get_name(guide_number):
    while True:
        name = input(f"Enter the name of guide #{guide_number}: ").strip()
        if name == "":
            print("No name entered.")
        else:
            return name

# creating a function that gets each guide's name and their boxes sold and stores them in lists
def get_guides(guides):
    names = []
    boxes = []
    for guide_number in range(1, guides + 1):
        print()
        name = get_name(guide_number)
        box_count = get_number(f"Enter the number of boxes sold by {name}: ", 0)
        names.append(name)
        boxes.append(box_count)
    return names, boxes

# calculates average boxes sold per guide
def calc_average(boxes, guides):
    return sum(boxes) / guides