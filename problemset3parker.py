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

# creating function that asks for a guides name and prompts an error message if entered incorrectly
def get_name(guide_number):
    while True:
        name = input(f"Enter the name of guide #{guide_number}: ").strip()
        if name == "":
            print("No name entered.")
        else:
            return name