def Fibonacci_sequence(n):
    F = []
    if n <= 2:
        i = 1
        while i <= n:
            F.append(1)
            i += 1
    else:
        F = [1,1]
        i = 3
        while i <= n:
            F.append(sum(F[-2:]))
            i += 1
    return F

print(Fibonacci_sequence(6))  
