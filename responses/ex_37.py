def word_splitter(word: str) -> int:
    return len(word.split())

with open("responses\words2.txt", "r") as txt_file:
    file_string = txt_file.read()
    file_string = file_string.replace("\n", "")
    file_string = file_string.replace(",", " ")
    print(f"Word in this string '{file_string}' = {word_splitter(file_string)}")