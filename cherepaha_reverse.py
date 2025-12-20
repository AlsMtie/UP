import csv

with open ("36031.csv", "r") as f:
    n = list(csv.reader(f))
    l=[]
    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)

l = l[-1::-1]
for i in range(len(l)):
    l[i] = l[i][-1::-1]

puti = []
for i in range(len(l)):
    stroki = []
    for j in range(len(l[i])):
        stroki.append('')
    puti.append(stroki)

def maxcoins(c):
    for i in range(len(c)):
        for j in range(len(c[i])):
            if (i == 0 and j == 0):
                continue
            elif (i == 0 and j != 0):
                c[i][j] = c[i][j] + c[i][j-1]
                puti[i][j] = puti[i][j-1] + " влево"
            elif (i != 0 and j == 0):
                c[i][j] = c[i][j] + c[i-1][j]
                puti[i][j] = puti[i-1][j] + " вверх"
            else:
                if c[i-1][j] > c[i][j-1]:
                    c[i][j] = c[i-1][j] + c[i][j]
                    puti[i][j] = puti[i-1][j] + " вверх"
                else:
                    c[i][j] = c[i][j-1] + c[i][j]
                    puti[i][j] = puti[i][j-1] + " влево"
            res = c[i][j]
            put = puti[i][j]
    return res, put

print(maxcoins(l))