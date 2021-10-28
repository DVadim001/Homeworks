def sum_range():
    print("Введите наименьшее число диапазона")
    num1 = int(input())
    print('введите наибольшее число диапазона')
    e = int(input())
    num2 = e+1
    sum = 0
    if num1 > num2:
        for i in range(num1, num2):
            sum = sum[::-1]
            sum -= i
        return sum
    else:
        for i in range(num1, num2):
            sum += i
        return(sum)
