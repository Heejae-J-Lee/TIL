def solution(s):
    answer = ''
    
    arr = list(map(int, s.split()))
    print(max(arr))
    answer = f'{min(arr)} {max(arr)}'
    
    return answer