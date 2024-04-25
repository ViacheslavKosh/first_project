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