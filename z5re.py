#1
"""def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1
    
print(factorial(7))"""

#2
"""def remove_vowels(string):
    glasnie = ["a", "y", "e", "u", "o", "i", "q"]
    string = list(string)
    for el in string:
        if el in glasnie:
            i = string.index(el)
            string[i] = " "
    result = ''.join(string)
    result = ''.join(result.split())
    return result
print(remove_vowels("qeadyuio"))"""

#3
"""def pascal(n):
    if n == 1:
        return [1]
    prosh_stroka = pascal(n - 1)
    new = [1]
    for i in range(len(prosh_stroka) - 1):
        new.append(prosh_stroka[i] + prosh_stroka[i + 1])
    new.append(1)
    return new

stroka = pascal(7)
result=[]
for el in stroka:
    result.append(str(el))
result = ' '.join(result)
print(result)"""