# Робота з часовими проміжками timedelta

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2)
print(delta)

from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

now = datetime.now()
future_date = now + timedelta(days = 10) # Додаємо 10 днів до дати
print(future_date)

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

a = timedelta()

print(a)