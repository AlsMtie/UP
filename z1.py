
#1
"""x1 = int(input("x1 = "))
y1 = int(input("x2 = "))
x2 = int(input("y1 = "))
y2 = int(input("y2 = "))

if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
    print("Ошибка")
else:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        print("Да")
    else:
        print("Нет")"""
    
#2 
"""K = int(input())
N = int(input())

ot = min(K, N)
do = max(K, N)

sum = 0
for i in range(ot, do+1):
    if i % 2 == 0:
        sum += i

print(sum)"""

#3
"""sum = 0
while True:
    n = int(input())
    if n == 0:
        break
    sum += n

print(sum)"""

#4
"""n = int(input())

if n < 0:
    print("ошибка")
else:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    print(fact)"""
