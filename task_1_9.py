# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print(a+b+c-min(a, b, c)-max(a, b, c), '- среднее')