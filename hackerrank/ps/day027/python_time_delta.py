import datetime

def time_delta(t1, t2):
    date1=datetime.datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    date2=datetime.datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    delta=int(abs(date1-date2).total_seconds())
    return str(delta)

t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)
    print(delta)
