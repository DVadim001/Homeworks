from func import *  # как лучше импортировать функцию (как правильно): в самом начале или непосредственно когда нужна?

print("Введите наименьшее число диапазона")
num1 = int(input())
print('введите наибольшее число диапазона')
e = int(input())
num2 = e+1


x = sum_range(num1, num2)
print('Сумма от {} до {} равна {}'.format(num1, e, x))
