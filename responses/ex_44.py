from string import ascii_lowercase

with open("responses/letters_44.txt", "w") as file_to_write:
    start_a = ascii_lowercase[::3]
    start_b = ascii_lowercase[1::3]
    start_c = ascii_lowercase[2::3]
    for letter1, letter2, letter3 in zip(start_a, start_b, start_c):
        file_to_write.write(f"{letter1}{letter2}{letter3}\n")