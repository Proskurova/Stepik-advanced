# Напишите программу для определения,
# является ли число произведением двух чисел из данного набора,
# выводящую результат в виде ответа «ДА» или «НЕТ».
n = int(input())
list_new = []
for i in range(n):
    k = int(input())
    list_new.append(k)
div = int(input())
yes = 0
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            if list_new[i]*list_new[j] == div:
                yes += 1
if yes > 0:
    print("ДА")
else:
    print("НЕТ")