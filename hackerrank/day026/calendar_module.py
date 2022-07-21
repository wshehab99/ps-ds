import calendar
def calendar_module(m,d,y):
    print(calendar.day_name[calendar.weekday(y,m,d)].upper())


m,d,y=map(int,input().split())
calendar_module(m,d,y)

