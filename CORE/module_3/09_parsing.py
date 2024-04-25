# Парсинг дати із рядка

from datetime import datetime

# Поточна дата та час
now = datetime.now()

format_datetime = now.strftime("%A, %d-%B-%Y, %H:%M:%S")
print(format_datetime)

date_string = "2024.03.08"
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

# Дата у вигляді рядка
iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()
print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# Отримання ISO календаря
iso_calendar = now.isocalendar()
print(iso_calendar)
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")