otvet = []

def f(n):
    if n[0] > n[1]:
        return f(n[1:])
    pervoe = n[0]
    otvet.append(pervoe)
    n = n[1:]
    min_n = n[0]
    ii = 0
    for i in range(n[0], len(n)-1):
        if n[i] < min_n and n[i] > pervoe:
            min_n = n[i]
            ii = i
    return f(n[ii:])

w = [6, 2, 5, 4, 7]

print(otvet)

#3
"""count = 0
for i in range(100, 1050):
    j = str(i)[::-1]
    if i + int(j) == 1050:
        count += 1
print(count)"""