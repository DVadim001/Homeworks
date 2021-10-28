# V 1

# def sum_range(start=int(input()), end=int(input())):
#     e = end+1
#     sum = 0
#     if start > e:
#         for i in range(e, start):
#             sum += i
#         return(sum)
#     else:
#         for i in range(start, e):
#             sum += i
#         return(sum)



# V 2

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
