def readable_timedelta(days):
    # insert your docstring here
    """This functions tells for the given number of days how many weeks and remaining days present.

    Args:
        days (int): Number of days for which you want to find how many weeks it combines to.

    Returns:
        str: Returns a string telling how many weeks and remaining days are present for the given number of days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


print(readable_timedelta.__doc__)