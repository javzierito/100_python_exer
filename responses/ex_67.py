d = dict(weather = "clima", earth = "terra", rain = "chuva") 
word_taken = input("Enter word:  ")
if word_taken in d:
    print(f"{d[word_taken]}")
else:
    print("That word doesnt exist!")