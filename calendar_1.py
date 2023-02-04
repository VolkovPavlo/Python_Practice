import calendar

# print(calendar.weekheader(3))
# print(calendar.firstweekday())

# print((calendar.month(2023, 1)))
# print(calendar.monthcalendar(2023, 1))

# print(calendar.calendar(2023))

day_of_the_week = calendar.weekday(2023, 1, 30)
print(day_of_the_week)

is_leap = calendar.isleap(2024)
print(is_leap)

how_many_leap_days = calendar.leapdays(2011, 2023)
print(how_many_leap_days)

