from math import sqrt

def is_prime(number):
    retVal = True
    for i in range(2, int(sqrt(number)) + 1):
        if ((number % i) == 0):
            retVal = False
            break
            
    return retVal

def recursive(numbers, set_numbers, checked, number, R):
    if (len(number) == R):
        set_numbers.add(int(number))
        
    for idx in range(len(numbers)):
        if checked[idx] != 1:
            checked[idx] = 1
            recursive(numbers, set_numbers, checked, number + numbers[idx], R)
            checked[idx] = 0
    
def solution(numbers):
    answer = 0
    
    set_numbers = set()
    
    checked = [0 for _ in range(len(numbers))]
    
    for r in range(len(numbers)):
        recursive(numbers, set_numbers, checked, "", r+1)
    
    for number in set_numbers:
        if 1 < number and is_prime(number):
            answer += 1
            
    return answer
