# На вход программе подается число n.
# Напишите программу, которая создает и выводит построчно вложенный список,
# состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
# Программа должна вывести построчно указанный вложенный список.
n = int(input())
list1 = [list(range(1, i+1)) for i in range(1, n + 1)]
for row in list1:
    print(row)