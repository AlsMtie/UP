#1

"""with open("27686.txt", "r") as f:
    stroka = f.readline()
max_dlina = 0
dlina = 0
for i in range(len(stroka)-1):
    if stroka[i] == "X":
        dlina += 1
        if dlina > max_dlina:
            max_dlina = dlina
    else:
        dlina = 0
print(max_dlina)"""

#2

"""with open("36037.txt", "r") as f:
    stroka = f.readline()

dlina = 0
max_dlina = 0
for i in range(len(stroka) - 3):
    if stroka[i] == "X" and stroka[i+1] == "Z" and stroka[i+2] == "Z" and stroka[i+3] == "Y":
        if dlina + 3 > max_dlina:
            max_dlina = dlina + 3
        dlina = 0
    else:
        dlina += 1
        if dlina > max_dlina:
            max_dlina = dlina
print(max_dlina)
"""
#3
"""with open("46982.txt", "r") as f:
    stroka = f.readline()
count = 0
i = 0
n = len(stroka)
while i < n:
    if stroka[i] == 'E':
        nachalo = i
        kones = i + 1
        f_count = 0 
        while kones < n and stroka[kones] != 'E':
            if stroka[kones] == 'F':
                f_count += 1
            kones += 1
        if kones < n and stroka[kones] == 'E':  
            dlina = kones - nachalo + 1
            if dlina >= 12 and f_count == 0: 
                count += 1
                i = kones
            else:
                i += 1
        else:
            i += 1
    else:
        i += 1
print(count)"""