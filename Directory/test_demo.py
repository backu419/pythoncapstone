import calendar, datetime, pytest


def cal(year, month):
    day_to_count = calendar.SUNDAY
    ma = calendar.monthcalendar(year, month)
    sundays = sum(1 for x in ma if x[day_to_count] != 0)
    return sundays

def key(n):
    dict={1:"sam",2:"sami", 3:"hemanth",4:"kumar"}
    for n in dict.keys():
        return True
    else:
        return False

def desc(l):
    l.sort(reverse=True)
    return l


def minn(l):
    l.sort(reverse=True)
    n = len(l)
    return l[n - 1]

