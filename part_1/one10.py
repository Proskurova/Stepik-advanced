# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
import re
n = int(input())
s = [input() for i in range(n)]
for i in s:
    if re.match(".*a.*n.*t.*o.*n.*", i):
        print(s.index(i)+1, end=" ")

