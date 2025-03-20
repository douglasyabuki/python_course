# Using calendar for calendars and dates
# https://docs.python.org/3/library/calendar.html
# calendar is used for general things related to calendars and dates.
# With calendar, you can find things like:
# - What is the last day of the month (e.g.: monthrange)
# - The name and number of the weekday for a given date (e.g.: weekday)
# - Generate a calendar itself (e.g.: monthcalendar)
# - Work with calendar-specific things (e.g.: calendar, month)
# By default, weekdays go from 0 to 6
# 0 = Monday | 6 = Sunday
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
# first_day_number, last_day = calendar.monthrange(2022, 12)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[first_day_number])
# print(calendar.day_name[calendar.weekday(2022, 12, last_day)])
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
