hour = '1h 45m,360s,25m,30m 120s,2h 60s'
count_min = 0
lst = hour.split(',')
for i in lst:
    minutes = i.split()
    for r in minutes:
        if 'h' in r:
            count_min += int(r.replace('h', '')) * 60
        elif 'm' in r:
            count_min += int(r.replace('m', ''))
        elif 's' in r:
            count_min += int(r.replace('s', '')) // 60

print(count_min)