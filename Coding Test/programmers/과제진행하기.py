def perform_task(time, playtime):
    hour, minute = map(int, time.split(':'))
    minute += int(playtime)
    hour += minute // 60
    minute = minute % 60
    
    return f"{hour}:{minute}"

def compare_time(time1, time2):
    hour1, minute1 = map(int, time1.split(':'))
    hour2, minute2 = map(int, time2.split(':'))
    
    diff_time = (hour1 - hour2) * 60 + (minute1 - minute2)
        
    return diff_time
    
def solution(plans):
    answer = []
    
    plans.sort(key = lambda x : int(x[1].replace(':','')))
    
    next_task = plans.pop(0)
    current_time = next_task[1]
    pending_tasks = []
    
    while True:
        if len(plans) == 0:
            break
        
        task_performed_time = perform_task(current_time, next_task[2])
        diff_time = compare_time(task_performed_time, plans[0][1])
        
        if diff_time <= 0:
            current_time = task_performed_time
            answer.append(next_task[0])
            next_task = plans.pop(0)
            
            while len(pending_tasks) != 0:
                next_pending_task = pending_tasks.pop()
                task_performed_time = perform_task(current_time, next_pending_task[2])
                diff_time = compare_time(task_performed_time, next_task[1])
                
                if diff_time <= 0:
                    current_time = task_performed_time
                    answer.append(next_pending_task[0])
                    
                else:
                    pending_tasks.append([next_pending_task[0],next_pending_task[1],str(diff_time)])
                    break
            current_time = next_task[1]
            
        else:
            pending_tasks.append([next_task[0], next_task[1], str(diff_time)])
            current_time = plans[0][1]
            next_task = plans.pop(0)
    
    current_time = perform_task(next_task[1], next_task[2])
    answer.append(next_task[0])
    
    while len(pending_tasks) != 0:
        current_time = perform_task(current_time, pending_tasks[-1][2])
        answer.append(pending_tasks[-1][0])
        pending_tasks.pop()
        
    return answer