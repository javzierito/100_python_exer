import os
letters_list = []
top_folder = "responses/letters"
for file in os.listdir(top_folder):
    with open(top_folder + "/" + file, "r") as file_handle:
        content = file_handle.read()
    letters_list.append(content.replace("\n", ""))

print(letters_list)