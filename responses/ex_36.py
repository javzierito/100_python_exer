def word_splitter(word: str) -> int:
    return len(word.split(" "))

with open("responses\words1.txt", "r") as txt_file:
    file_string = txt_file.read()
    print(f"Word in this string '{file_string}' = {word_splitter(file_string)}")