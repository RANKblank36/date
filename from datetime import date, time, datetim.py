from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("current date and time:", now)
print("\nDate components:", today.year, today.month, today.day)