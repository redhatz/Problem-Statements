import calendar
from datetime import datetime

dates={'2020-01-06':8,'2020-01-05':14,'1970-01-10':4,'2100-01-01':2500,'2090-05-20':30000}

print("Input Dates and values")
print(dates)
result = dict(zip(calendar.day_name, [0] * 7))
for dateStr, value in dates.items():
    result[datetime.strptime(dateStr, "%Y-%m-%d").strftime("%A")] += int(value)

print("Output")
print(result)