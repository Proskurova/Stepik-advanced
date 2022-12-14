# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
# верхнюю, нижнюю, левую и правую.
# Напишите программу, которая вычисляет сумму элементов: верхней четверти;
# правой четверти; нижней четверти; левой четверти.
# Формат входных данных:
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
# Формат выходных данных:
# Программа должна вывести текст в соответствии с условием задачи.
# Примечание. Элементы диагоналей не учитываются.
n = int(input())
matrix = [input().split(" ") for _ in range(n)]
upper_quarter, lower_quarter, left_quarter, right_quarter = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if j > i < (n - 1 - j):
            upper_quarter += int(matrix[i][j])
        elif j < i > (n - 1 - j):
            lower_quarter += int(matrix[i][j])
        elif j < i < (n - 1 - j):
            left_quarter += int(matrix[i][j])
        elif j > i > (n - 1 - j):
            right_quarter += int(matrix[i][j])
print(f"Верхняя четверть: {upper_quarter}\nПравая четверть: {right_quarter}\n"
      f"Нижняя четверть: {lower_quarter}\nЛевая четверть: {left_quarter}")