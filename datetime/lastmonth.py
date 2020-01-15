#!/usr/bin/env python3
import sys
import os
import delorean
import datetime
import calendar


def test_arithmetic(today):
    print("Today = {}".format(today))
    print("Today's month = {}".format(today.datetime.month))
    print("Today's day of month = {}".format(today.datetime.day))
    print("Today (trunc. to month) = {}".format(today.truncate('month')))

    last_month = today - datetime.timedelta(days=(today.datetime.day+1))

    print("Last month = {}".format(last_month.datetime.month))
    print("Last month's year = {}".format(last_month.datetime.year))

    # calendar.monthrange() returns weekday of the first day of the month
    # and the number of days in the month for the given year & month
    print("Month range = {}".format(calendar.monthrange(last_month.datetime.year, last_month.datetime.month)))
    print("--------------------------------")



today = delorean.Delorean()
test_arithmetic(today)

today = delorean.parse("2020/2/1 00:00:00", dayfirst=False)
test_arithmetic(today)

today = delorean.parse("2020/3/2 00:00:00", dayfirst=False)
test_arithmetic(today)

today = delorean.parse("2021/1/2 00:00:00", dayfirst=False)
test_arithmetic(today)

