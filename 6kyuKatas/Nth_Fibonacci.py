def nth_fib(n):
    a,b = 0,1
    fibo = [a,b]
    print(fibo)
    if n==1:
            return a
    if n==2:
            return b
    else:
        for i in range(0, n):
            c = a+b
            d = b+c
            a,b,c = b,c,d 
            fibo.append(d)
        result = fibo[n-2]
        return result 