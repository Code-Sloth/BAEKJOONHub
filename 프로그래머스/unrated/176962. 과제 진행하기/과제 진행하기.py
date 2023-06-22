def solution(plans):
    answer = []
    stop = []
    plan = sorted(plans, key=lambda x:x[1])

    for i in range(len(plan) - 1):
        time = (int(plan[i][1].split(':')[0]) - int(plan[i+1][1].split(':')[0]))*60 + (int(plan[i][1].split(':')[1]) - int(plan[i+1][1].split(':')[1]))
        remain_time = int(plan[i][2]) + time

        if remain_time > 0:
            stop.append([plan[i][0], remain_time])
        else:
            answer.append(plan[i][0])
            while stop and remain_time < 0:
                remain_time += stop[-1][1]
                if remain_time > 0:
                    stop[-1][1] = remain_time
                else:
                    answer.append(stop.pop()[0])

    answer.append(plan[-1][0])
    for s in stop[::-1]:
        answer.append(s[0])

    return answer