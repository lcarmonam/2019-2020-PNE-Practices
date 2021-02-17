def fibosum(n):
    series = [0, 1, 1]
    a = 1
    b = 1
    for i in range(1, n - 1):
        c = b + a
        series.append(c)
        a = b
        b = c
    return series


print("Sum of the first 5 terms of the Fibonacci series: ", sum(fibosum(5)))
print("Sum of the first 10 terms of the Fibonacci series: ", sum(fibosum(10)))