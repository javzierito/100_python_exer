import os
letters_list = []
top_folder = "responses/letters"
list_to_check = ["p", "y", "t", "h", "o", "n"]
for file in os.listdir(top_folder):
    if file.split(".")[0] in list_to_check:
        with open(top_folder + "/" + file, "r") as file_handle:
            content = file_handle.read()
        letters_list.append(content.replace("\n", ""))

print(letters_list)