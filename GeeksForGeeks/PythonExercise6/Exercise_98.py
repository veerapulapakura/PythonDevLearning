# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
#
# 08 05 2015

import calendar

month, day, year = map(int, input().split())
dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())








