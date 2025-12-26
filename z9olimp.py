#1
"""def firstmin(n):
    if len(n) > 1 and n[0] > n[1]:
        return firstmin(n[1:])
    return n
def f(n):
    if not n:
        return
    if not otvet:
        otvet.append(n[0])
    min_n = None
    idx_min = None
    for i in range(len(n)):
        if n[i] > otvet[-1]:
            if min_n is None or n[i] < min_n:
                min_n = n[i]
                idx_min = i
    if idx_min:
        otvet.append(min_n)
        f(n[idx_min:])
n = [6, 2, 5, 4, 2, 5, 6]
otvet = []
print(n)
n = firstmin(n)
f(n)
print(otvet)"""


#2
"""def firstmin(n):
    if len(n) > 1 and n[0] > n[1]:
        return firstmin(n[1:])
    return n
def posl(n):
    if not n:
        return
    if not otvet:
        otvet.append(n[0])
    min_n = None
    idx_min = None
    for i in range(len(n)):
        if n[i] > otvet[-1]:
            if min_n is None or n[i] < min_n:
                min_n = n[i]
                idx_min = i
    if idx_min:
        otvet.append(min_n)
        posl(n[idx_min:])
with open('r.txt', 'r') as f:
      l = f.readlines()
l = str(l[1])
l = l.split()
spisok = []
for el in l:
    spisok.append(int(el))
n = firstmin(spisok)
otvet = []
posl(n)
with open("o.txt", "w") as f:
    f.write(f"{len(otvet)}")
print(len(otvet))"""
#3
"""count = 0
for i in range(100, 1050):
    j = str(i)[::-1]
    if i + int(j) == 1050:
        count += 1
print(count)"""
