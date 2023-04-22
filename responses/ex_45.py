from string import ascii_lowercase

for letter in ascii_lowercase:
    with open(f"responses/{letter}.txt", "w") as file_to_write:
        file_to_write.write(f"{letter}\n")