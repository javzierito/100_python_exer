from datetime import datetime
currentYear = datetime.now().year
user_age = int(input("Give me your age: "))
print(f"We think you were born in {currentYear - user_age}")