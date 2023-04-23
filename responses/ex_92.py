import os

file_number = 0

for file in os.listdir("responses/filesfiles"):
    if file.endswith(".py"):
        file_number += 1

print(file_number)