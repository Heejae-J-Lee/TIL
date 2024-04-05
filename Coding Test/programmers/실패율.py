def solution(N, stages):
    answer = []
    state_percentage_failure = [0 for _ in range(N)]
    people = len(stages)
    
    for stage in stages:
        if N < stage:
            continue
        idx = stage-1
        state_percentage_failure[idx] += 1
    
    prev_level_people = 0
    for idx, failure in enumerate(state_percentage_failure):
        people -= prev_level_people
        prev_level_people = state_percentage_failure[idx]
        if state_percentage_failure[idx] == 0:
            state_percentage_failure[idx] = [0, idx+1]
            continue
        state_percentage_failure[idx] = [state_percentage_failure[idx] / people, idx+1]
        
    state_percentage_failure.sort(key = lambda x : (-x[0], x[1]))
    for stage_and_failure in state_percentage_failure:
        answer.append(stage_and_failure[1])
    
    return answer