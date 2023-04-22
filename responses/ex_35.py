def word_splitter(word: str) -> int:
    return len(word.split())

string1 = "carlos alberto buenafuente jubrick"
print(f"Word in this string '{string1}' = {word_splitter(string1)}")