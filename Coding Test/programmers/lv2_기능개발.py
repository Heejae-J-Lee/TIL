def solution(progresses, speeds):
    answer = []
    queue = []
    
    for idx, progress in enumerate(progresses):
        days = 0
        while progress + (days * speeds[idx]) < 100:
            days += 1
        queue.append(days)
    
    day = 0
    deploy = 0
    while True:
        if len(queue) == 0:
            answer.append(deploy)
            break

        if queue[0] <= day:
            deploy += 1
        else:
            if deploy != 0:
                answer.append(deploy)
            day = queue[0]
            deploy = 1
        queue.pop(0)
        
    return answer