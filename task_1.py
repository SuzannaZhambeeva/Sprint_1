time_s = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minuts = 0
time_parts = time_s.split(',')
for i in time_parts:
    units = i .strip().split()
    for j in units:
        if 'h' in j:
            total_minuts += int(j.replace('h', '')) * 60
        elif 'm' in j:
            total_minuts += int(j.replace('m', ''))
        elif 's' in j:
            total_minuts += int(j.replace('s', '')) // 60
print(total_minuts)