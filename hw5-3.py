import calendar

# Question 1

calendar.TextCalendar().pryear(2020)

# Question 2

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.calendar(2020))

# Question 3

calendar.prmonth(2003,1)

# Question 4

#calendar.LocaleTextCalendar(6, "SPAINISH").pryear(2020)

# Question 5

print(calendar.isleap(2003))

# It determines if the given year is a leap year of not. It returns True of False as a result, it is a boolean value.
