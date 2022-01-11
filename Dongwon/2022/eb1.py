from collections import defaultdict
from itertools import product
def solution(schedule):
    arr = list(product(*schedule))
    result = 0
    for item in arr:
        day_dict = defaultdict(list)
        for jtem in item:
            ktem = jtem.split(" ")
            if len(ktem) == 2:
                day, time = ktem
                time = trans_minute(time, False)
                if not day_dict[day]:
                    day_dict[day].append(time)
                else:
                    day_dict[day].split("~")
            else:
                day, time, day2, time2 = ktem
                time = trans_minute(time, True)
                time2 = trans_minute(time2, True)
                if not day_dict[day]:
                    day_dict[day].append(time)
                    day_dict[day2].append(time2)
        print(day_dict)

def trans_minute(time, half):
    t, m = time.split(":")
    start = int(t) * 60 + int(m)
    end = start + (90 if half else 180)
    
    return str(start) + "~" + str(end)





solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]])
