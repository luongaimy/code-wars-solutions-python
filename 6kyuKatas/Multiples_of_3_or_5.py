def solution(number):
    Sum = 0
    for i in range(0,number):
        if (i%3==0) and (i%5==0):
            Sum += i
        elif (i%3==0):
            Sum += i
        elif (i%5==0):
            Sum += i
            
    return Sum
