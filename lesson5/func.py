def sum_range(num1, num2):
    sum = 0
    if num1 > num2:
        sum = int()
        sum = sum[::-1]
        for i in range(num1, num2):
            sum = sum + i
        return sum
    else:
        for i in range(num1, num2):
            sum += i
        return(sum)
