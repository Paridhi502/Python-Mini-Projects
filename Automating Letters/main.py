
with open("./Input/Names/invited_names.txt") as invited_names:
    # Return all lines in the file, as a list where each line is an item in the list object
    names = invited_names.readlines()
    print(names)
    i = 0
    for name in names:
        stripped_name = name.strip()
        names[i] = stripped_name
        i = i + 1
    print(names)
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        # read() stores as a string
        send_letter = starting_letter.read()
        for name in names:
            new_letter = send_letter.replace("[name]", name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as sending_letter:
                sending_letter.write(new_letter)

