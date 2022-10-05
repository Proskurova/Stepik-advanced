# На вход программе подается натуральное число n.
# Напишите программу, которая выводит первые n строк треугольника Паскаля.
# Формат входных данных:
# На вход программе подается число n (n≥1).
# Формат выходных данных:
# Программа должна вывести первые nn строк треугольника Паскаля,
# каждую на отдельной строке в соответствии с образцом.
n = int(input())
list1 = [[0]*i for i in range(1, n+2)]
for i in range(n+1):
    for j in range(i):
        if j == 0 or j == i:
            list1[i][j] = 1
        else:
            list1[i][j] = list1[i-1][j-1] + list1[i-1][j]
        print(list1[i][j], end=' ')
    print()
