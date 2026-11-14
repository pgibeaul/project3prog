# creating a function that asks for a phrase and prompts them to try again if they type nothing
def get_phrase():
    while True:
        phrase = input("Type a phrase (or quit to exit program): ").strip()
        if phrase == "":
            print("Type a phrase (or quit to exit program): ")
        else:
            return phrase


