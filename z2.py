#1
"""n = int(input())
if (n <= 0):
    print("Ошибка")
else:
    l = [0, 1]
    for i in range(n-2):
        new_el = l[0] + l[1]
        l[0] = l[1]
        l[1] = new_el
    print(l[1])"""
    
    
#2 
"""n = int(input())
if (n <= 0):
    print("Ошибка")
else:
    if (n == 1):
        print(1)
    elif (n == 2):
        print(1)
    elif (n == 3):
        print(2)
    else:
        l = [1, 1, 2]
        for i in range(n-3):
            new_el = l[0] + l[1] + l[2]
            l[0] = l[1]
            l[1] = l[2]
            l[2] = new_el
        print(l[2])"""

    
#3
"""c = [
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 40, 70, 0, 0, 1],
        [100, 0, 0, 0, 0, 1]
        ]
puti = []
for i in range(len(c)):
    stroki = []
    for j in range(len(c[i])):
        stroki.append('')
    puti.append(stroki)
    
def maxcoins(c):
    for i in range(len(c)):
        for j in range(len(c[i])):
            if (i==0 and j==0):
                continue
            elif (i == 0 and j != 0):
                c[i][j] = c[i][j]+c[i][j-1]
                puti[i][j] = puti[i][j-1] + " вправо"
            elif (i !=0 and j == 0):
                c[i][j] = c[i][j] + c[i-1][j]
                puti[i][j] = puti[i-1][j] + " вниз"
            else:
                if c[i-1][j] > c[i][j-1]:
                    c[i][j] = c[i-1][j] + c[i][j]
                    puti[i][j] = puti[i-1][j] + " вниз"
                else:
                    c[i][j] = c[i][j-1] + c[i][j]
                    puti[i][j] = puti[i][j-1] + " вправо"
            res = c[i][j]
            put = puti[i][j]
    return res, put
print(maxcoins(c))"""