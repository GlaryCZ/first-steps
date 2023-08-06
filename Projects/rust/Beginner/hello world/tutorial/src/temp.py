def totalWaysToSum(n):
    sum = 0
    if n == 1:
        return 1
    else:
        f = 1
        while n > f:
            sum += totalWaysToSum(f)
            f += 1
        return sum
    
print(totalWaysToSum(55))

