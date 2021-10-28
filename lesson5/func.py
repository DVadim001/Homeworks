def sum_range(num1, num2):
    sum = 0
    if num1 > num2:
        for i in range(num2-1, num1+1):
            sum = sum + i
        return sum
    else:
        for i in range(num1, num2):
            sum += i
        return(sum)
