def fibon(n):
    series = [0, 1, 1]
    a = 1
    b = 1
    for i in range(1, n - 1):
        c = b + a
        series.append(c)
        a = b
        b = c
        number = series[-1]
    #return number
    return c


print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))