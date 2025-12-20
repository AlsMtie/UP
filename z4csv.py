#1
"""1.	59778 Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел. 
Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
среди семи чисел совпадают ровно четыре числа;
среднее значение неповторяющихся чисел больше суммы повторяющихся чисел.
"""
"""import csv


with open ("59778.csv", "r") as f:
    n = list(csv.reader(f))
    l=[]
    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
c_strok=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i].count(l[i][j])==4:
            repeat = l[i][j]
            x = []
            for j in range(len(l[i])):
                if l[i][j] not in x and l[i][j] != repeat:
                    x.append(l[i][j])
            summa_repeat = repeat * 4
            average_sum = sum(x) / 3
            if average_sum > summa_repeat:
                c_strok+=1
print(c_strok//4)
"""

#2 Дана последовательность вещественных чисел.
# Из неё необходимо выбрать несколько подряд идущих чисел так,
# чтобы каждое следующее число было меньше предыдущего.
# Какую максимальную сумму могут иметь выбранные числа?

"""import csv
with open ("29666.csv", "r") as f:
    n = list(csv.reader(f))
    for i in range(len(n)):
        n[i] = float(n[i][0] + "." + n[i][1])
max_summa = n[0]
summa = n[0]
for i in range(len(n)):
    if n[i] < n[i-1]:
        summa += n[i]
    else:
        summa = n[i]

    if summa > max_summa:
        max_summa = summa

print(max_summa)
"""