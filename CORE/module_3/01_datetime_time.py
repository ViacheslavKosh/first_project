# Модулі datetime та time. Робота з випадковими величинами. Модуль math.

# Робота з датою
import datetime

now = datetime.datetime.now()
print (now)
print(datetime.datetime.now())

from datetime import datetime
current_datrtime = datetime.now()
print(f"Now is {current_datrtime.year} year", end=" ")
print(f"{current_datrtime.month} month", end=" ")
print(f"{current_datrtime.day} day")
print(f"{current_datrtime.hour} hours")
print(f"{current_datrtime.minute} minutes")
print(f"{current_datrtime.second} seconds")
print(f"{current_datrtime.microsecond} microseconds")
print(f"X3 4E 3A {current_datrtime.tzinfo}")
print(current_datrtime.date())
print(current_datrtime.time())