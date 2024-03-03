# Модулі datetime та time. Робота з випадковими величинами. Модуль math.

# Робота з датою
import datetime

# now = datetime.datetime.now()
# print (now)
# print(datetime.datetime.now())

# from datetime import datetime
# current_datrtime = datetime.now()
# print(f"Now is {current_datrtime.year} year", end=" ")
# print(f"{current_datrtime.month} month", end=" ")
# print(f"{current_datrtime.day} day")
# print(f"{current_datrtime.hour} hours")
# print(f"{current_datrtime.minute} minutes")
# print(f"{current_datrtime.second} seconds")
# print(f"{current_datrtime.microsecond} microseconds")
# print(f"X3 4E 3A {current_datrtime.tzinfo}")
# print(current_datrtime.date())
# print(current_datrtime.time())

# party_date = datetime.date(2024, 3, 8)
# party_time = datetime.time(12, 10, 00)
# combined_datetime = datetime.datetime.combine(party_date, party_time)
# print(combined_datetime)
# spesific_date = datetime.datetime(year=2024, month=3, day=18)
# print(spesific_date)
# spesific_date = datetime.datetime(year=2024, month=3, day=18, hour=14, minute=12)
# print(spesific_date)
# spesific_date = datetime.datetime(2024, 3, 18, 14, 12)
# print(spesific_date)

# from datetime import datetime
# now = datetime.now()
# day_of_weeek = now.weekday()
# print(f"Its a {day_of_weeek} day of week")

# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# Робота з часовими проміжками timedelta

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2)
# print(delta)

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0

# now = datetime.now()
# future_date = now + timedelta(days = 10) # Додаємо 10 днів до дати
# print(future_date)

# from datetime import datetime, timedelta

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

from datetime import datetime
year = int(input("Enter your year of birth: "))
month = int(input("Enter month of your birth: "))
day = int(input("Enter day of your birth: "))
birth_date = datetime(year, month, day)
now = datetime.now()
difference = now-birth_date 
original_date = birth_date.toordinal()
print(f"You born in {original_date} day after birth of Jesus Christ")
print(f"You are live {difference} hours on Earth")