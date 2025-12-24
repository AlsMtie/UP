#1
"""ss15 = '0123456789ABCDE'
def fifit(n):
    res = []
    while n != 0:
        res.append(ss15[n % 15])
        n = n // 15
    res.reverse()
    return "".join(res)

otvet = 0
for el in ss15:
    a = '123'
    b = '233'
    res = int((a+el+'5'), 15) + int(("1"+el+b), 15)
    if res % 14 == 0:
        otvet = res // 14
        break
print(otvet)
print(fifit(otvet))"""


#2
"""otvet = 0
for i in range(16, 100):
    a = 10 * i**6 + 11 * i**5 + 2 * i **4 + 6 * i ** 3 + 7 * i **2 + 13 * i **1 + 1 * i ** 0
    b = 15 * i**6 + 0 * i**5 + 2 * i **4 + 4 * i ** 3 + 10 * i **2 + 8 * i **1 + 9 * i ** 0
    if (a + b) % (i - 1) == 0:
        otvet = i
        break
print(otvet)"""

#3
"""res = 0
for i in range(10):
    a = int(str(i)+'B09', 17)
    b = int(str(i) + '8E8', 15)
    if (a+b) % 155 == 0:
        res = (a + b) // 155
        break
print(res)"""



#4
"""otv = []
for x in '01234567':
    for y in '01234567':
        res = int(y + '04' + x+'5', 11) + int('253' + x + y, 8)
        if res % 117 == 0:
            otv.append(res)
if otv:
    print(min(otv) // 117)"""

#5
"""n = 7* 512**1912 + 6* 64**1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022
otvet = []
while n != 0:
    otvet.append(str(n % 8))
    n = n // 8
otvet.reverse()
s = "".join(otvet)
c = 0
for el in s:
    if el == "7":
        c += 1
print(c)"""