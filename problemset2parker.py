# creating a function that asks for a phrase and prompts them to try again if they type nothing
def get_phrase():
    while True:
        phrase = input("Type a phrase (or quit to exit program): ").strip()
        if phrase == "":
            print("Enter a phrase.")
        else:
            return phrase

# creating a function that asks what letters to redact and checks if they're valid then returns them as a list
def get_redact_letters():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        letters = input("Type a comma-separated list of letters to redact: ")
        letter_list = []
        valid = True
        for char in letters:
            if char.lower() in alphabet:
                letter_list.append(char.lower())
            elif char not in ", ":
                valid = False
        if valid and not letter_list == []:
            return letter_list
        print("Enter letters separated by commas only.")