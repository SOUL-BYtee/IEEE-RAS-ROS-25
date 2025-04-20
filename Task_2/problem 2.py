from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

today = datetime(year, month, day)
tomorrow = today + timedelta(days=1)

print(f"Day: {tomorrow.day} Month: {tomorrow.month} Year: {tomorrow.year}")