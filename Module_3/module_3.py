

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

# from datetime import datetime
# year = int(input("Enter your year of birth: "))
# month = int(input("Enter month of your birth: "))
# day = int(input("Enter day of your birth: "))
# birth_date = datetime(year, month, day)
# now = datetime.now()
# difference = now-birth_date 
# original_date = birth_date.toordinal()
# print(f"You born in {original_date} day after birth of Jesus Christ")
# print(f"You are live {difference} hours on Earth")

# timestamp = datetime.timestamp(now)
# print(timestamp)

# from datetime import datetime

# # Припустимо, є timestamp
# timestamp = 1917183600

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime

# Парсинг дати із рядка

# from datetime import datetime
# # Поточна дата та час
# now = datetime.now()
# format_datetime = now.strftime("%A, %d-%B-%Y, %H:%M:%S")
# print(format_datetime)
# date_string = "2024.03.08"
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)
# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)
# # Дата у вигляді рядка
# iso_date_string = "2023-03-14T12:39:29.992996"
# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)
# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()
# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня
# # Отримання ISO календаря
# iso_calendar = now.isocalendar()
# print(iso_calendar)
# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# Робота з часовими зонами

from datetime import datetime, timezone, timedelta
local_now = datetime.now()
utc_local = datetime.now(timezone.utc)
eastern_time = utc_local.astimezone(timezone(timedelta(hours=-5)))
print(local_now)
print(utc_local)
print(eastern_time)

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

