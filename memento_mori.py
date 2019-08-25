#!/usr/local/bin/python3

from datetime import date, timedelta

# your birthdate
birthday = date(1990, 8, 8)

# average life expectancy in your country for your gender, 
# check https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy
life_expectancy_days = 365 * 81.3  # years

# offset the year line by the weekday of the first day,
# e.g. if the first of January is a Wednesday, the line will be offset by 2
# this will make each column the same weekday over all lines
enable_weekday_offset = False

# show the year to the left of the line
show_year = True

# character displayed for a day you have lived
day_passed = '▮'

# character displayed for a day
day_future = '·'

birth_year = birthday.year
day_of_birthyear = (birthday - date(birthday.year, 1, 1)).days

now = date.today()
year_now = now.year
day_of_year_now = (now - date(year_now, 1, 1)).days

date_of_death = birthday + timedelta(days=life_expectancy_days)
day_of_deathyear = (date_of_death - date(date_of_death.year, 1, 1)).days
days_left = life_expectancy_days


def days_in_year(year):
    return (date(year + 1, 1, 1) - date(year, 1, 1)).days


def weekday_offset(year):
    return date(year, 1, 1).weekday() if enable_weekday_offset else 0


output = []

output += [(birth_year, weekday_offset(birth_year) + day_of_birthyear, 
    days_in_year(birth_year) - day_of_birthyear, 0)]

for y in range(birth_year+1, year_now-1):
    output += [(y, weekday_offset(y), days_in_year(y), 0)]

output += [(year_now, weekday_offset(y), day_of_year_now, days_in_year(year_now) - day_of_year_now)]

for y in range(year_now+1, date_of_death.year-1):
    output += [(y, weekday_offset(y), 0, days_in_year(year_now))]

output += [(date_of_death.year, weekday_offset(y), 0, day_of_deathyear)]


for year, offset, past, future in output:
    print('{year} {offset}{past}{future}'.format(
        year=year if show_year else '',
        offset=''.join([' ' for _ in range(offset)]),
        past=''.join([day_passed for _ in range(past)]), 
        future=''.join([day_future for _ in range(future)])))
