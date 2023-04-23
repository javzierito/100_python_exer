import string

def check_digits(string_text):
    for digit in string.digits:
        if digit in string_text:
            return True
    print("wrong pass, no numbers in it")
    return False

def check_uppers(string_text):
    for uppers in string.ascii_uppercase:
        if uppers in string_text:
            return True
    print("wrong pass, no uppercases in it")
    return False

def check_len(string_text):
    if len(string_text) >= 5:
        return True
    print("wrong lenght, should be 5 or more chars")
    return False

while 1:
    user_pass = input("give me your pass, let's check if it is alright: ")
    if len(user_pass) >= 5 and check_digits(user_pass) and check_uppers(user_pass):
        print("Pass fine")
        break
    else: 
        print("Pass not fine")
    