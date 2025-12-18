#1
"""with open("39762.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]
count = 0
summa = 0
for i in range(len(n)-1):
    if (n[i]*n[i+1])%15 == 0 and (n[i]+n[i+1])%7 == 0:
        count += 1
        if summa < n[i] + n[i +1] :
            summa = n[i] + n[i + 1]

print(count, summa)
"""


#2
"""with open("68279.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]
    max_el = 0
    for el in n:
        if str(el)[-3:] == '562':
            if max_el < el:
                max_el = el
count = 0
max_sum = 0

for i in range(len(n)-3):
    n1 = n[i]
    n2 = n[i+1]
    n3 = n[i+2]
    n4 = n[i+3]

    pytizn = 0
    nepytizn = 0
    kr3 = 0
    kr7 = 0
    summa = n1 + n2 + n3 + n4

    for el in [n1, n2, n3, n4]:
        if 10000 <= el <= 99999:
            pytizn += 1
        else:
            nepytizn += 1
        if el % 3 == 0:
            kr3 += 1
        if el % 7 == 0:
            kr7 += 1

    if pytizn >= 1 and nepytizn >= 2 and kr3 < kr7 and max_el < summa < 2 * max_el:
        count += 1
        if max_sum < summa:
            max_sum = summa
print(count, max_sum)
"""

#3
with open("40992.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]

count = 0
sum = 0
for el in n:
    if el % 2 != 0:
        count += 1
        sum+= el
sr_orif = sum //count

c = 0
max_sum = 0
for i in range(len(n) - 1):
    if (n[i] % 5 == 0 or n[i + 1] % 5 == 0) and (n[i] < sr_orif or n[i + 1] < sr_orif):
        c += 1
        if n[i] + n[i + 1] > max_sum:
            max_sum = n[i] + n[i + 1]

print(c, max_sum)