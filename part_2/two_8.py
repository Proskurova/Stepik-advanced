# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов,
# имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы.
# Каждое число равно сумме двух расположенных над ним чисел.
# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....
# На вход программе подается число n. Напишите программу,
# которая возвращает указанную строку треугольника Паскаля в виде списка
# (нумерация строк начинается с нуля).
# Программа должна вывести указанную строку треугольника Паскаля в виде списка.
n = int(input())
list1 = [[1]*i for i in range(1, n+2)]
for i in range(n+1):
    for j in range(i):
        if j == 0 or j == i:
            pass
        else:
            list1[i][j] = list1[i-1][j-1] + list1[i-1][j]
print(list1[n])



