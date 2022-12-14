from datetime import date, time


def is_high_season(date_time):
    """Find whether a datetime is considered as high season.

    Return 1 if datetime is between Dec-15 and Mar-3, 
    or between Jul-15 and Jul-31, or between Sep-11 and Sep-30. 
    Return 0 otherwise.

    """
    year = date_time.year
    if (date_time.date() > date(year, 3, 3) and date_time.date() < date(year, 7, 15)) or \
            (date_time.date() > date(year, 7, 31) and date_time.date() < date(year, 9, 11)) or \
            (date_time.date() > date(year, 9, 30) and date_time.date() < date(year, 12, 15)):
        return 0
    else:
        return 1


def get_period_day(date_time):
    """Return the period of day for a datetime object.

    There are 3 possible periods of day:
    morning - between 5:00 and 11:59, 
    afternoon - between 12:00 and 18:59, 
    night - between 19:00 and 4:59.
    """
    if date_time.time() >= time(5, 0, 0) and date_time.time() < time(12, 0, 0):
        return "morning"
    elif date_time.time() >= time(12, 0, 0) and date_time.time() < time(19, 0, 0):
        return "afternoon"
    else:
        return "night"
