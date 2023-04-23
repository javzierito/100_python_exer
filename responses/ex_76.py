from datetime import datetime
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
print(f"Today is {datetime.today().strftime('%A')}, {month} {day}, {year}")