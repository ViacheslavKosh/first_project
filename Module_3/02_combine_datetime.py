import datetime

party_date = datetime.date(2024, 3, 8)
party_time = datetime.time(12, 10, 00)
combined_datetime = datetime.datetime.combine(party_date, party_time)
print(combined_datetime)