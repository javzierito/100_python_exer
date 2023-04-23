with open("responses/text11.txt", "r") as file_handler:
    text1 = file_handler.read()

with open("responses/text12.txt", "r") as file_handler:
    text2 = file_handler.read()
new_list = text1.replace("\n", " ").split() + text2.replace("\n", " ").split()[1:]
for text_line in new_list:
    print(text_line)