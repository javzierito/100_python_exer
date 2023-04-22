from string import ascii_lowercase

with open("responses/letters_43.txt", "w") as file_to_write:
    start_a = ascii_lowercase[::2]
    start_b = ascii_lowercase[1::2]
    for letter1, letter2 in zip(start_a, start_b):
        file_to_write.write(f"{letter1}{letter2}\n")