from datetime import datetime
from datetime import timedelta

def solution(arr):
    inp = []
    for log in arr:
        s = log.split(" ")
        end = datetime.fromisoformat(s[0] + " " + s[1])
        t_diff = timedelta(seconds=(float(s[2][:-1]) - 0.001))
        start = end - t_diff
        inp.append((start, end))
    max_count = 0
    for  i in range(len(inp)):

        for k in range(2):
            count = 1
            local_start = inp[i][k]
            local_end = inp[i][k] + timedelta(seconds=1-0.001)

            for j in range(len(inp)):

                if j == i:
                    continue

                if (local_start <= inp[j][0] <= local_end) or (local_start <= inp[j][1] <= local_end) or (inp[j][0] <= local_start and inp[j][1] >= local_end):
                    count += 1

            max_count = max(max_count, count)

    return max_count