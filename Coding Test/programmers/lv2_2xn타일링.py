'''
f(n) = 길이가 n인 직사각형을 만드는 방법의 수
n = 0, f(0) = 1 # 방법은 없지만 초깃값 역할을 함
n = 1, f(1) = 1
n = 2, f(2) = f(1) + f(0) = 1
n = 3, f(3) = f(2) + f(1) = 2
n = 4, f(4) = f(3) + f(2) = 3
n = m, f(m) = f(m-1) + f(m-2)
'''

def solution(n):
    answer = 0
    
    fn = [1, 1]
    
    while True:
        if len(fn) == n+1:
            break
        fn.append((fn[-1] + fn[-2])%1000000007)
        
    answer = fn[n]
    
    return answer