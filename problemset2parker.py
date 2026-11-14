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

# creating a function that replaces the chosen letters with underscores and counts how many were replaced
def get_redact_phrase(phrase, letter_list):
    redacted = ""
    count = 0
    for char in phrase:
        if char.lower() in letter_list:
            redacted += "_"
            count += 1
        else:
            redacted += char
    return redacted, count

# creating main function to run the program and continue redacting phrases until the user types quit
def main():
    phrase = get_phrase()
    while not phrase.lower() == "quit":
        print()
        letter_list = get_redact_letters()
        redacted, count = get_redact_phrase(phrase, letter_list)
        print(f"Number of letters redacted: {count}")
        print(f"Redacted phrase: {redacted}")
        print()
        phrase = get_phrase()

main()