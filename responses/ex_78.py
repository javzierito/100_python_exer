import random
import string

all_strings = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

random_selection = random.sample(all_strings, 6)
print(random_selection)