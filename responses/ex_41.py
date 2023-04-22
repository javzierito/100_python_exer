from string import ascii_lowercase

with open("responses/letters_41.txt", "w") as file_to_write:
    for letter in ascii_lowercase:
        file_to_write.write(f"{letter}\n")