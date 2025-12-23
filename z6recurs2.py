#1

"""def N(x, y): 
    if x>y:
        return 0
    if x == y:
        return 1
    else:
        perviy = N(x+1, y)
        vtoroy = N(x+2, y)
        tretiy = N(x*2, y)
        res = perviy + vtoroy + tretiy
        return res

ot3do10 = N(3, 10)
ot10do12 = N(10, 12)
print(ot3do10 * ot10do12)"""

#2

"""def f(x, y):
    if x>y:
        return 0
    if x == 26:
        return 0 
    if x == y:
        return 1
    else:
        perviy = f(x+1, y)
        vtoroy = f(2*x+1, y)
        res = perviy + vtoroy
        return res
print(f(1,27))"""

#3
"""def S(x, y):
    if x>y:
        return 0 
    if x == 14:
        return 0
    if x == y:
        return 1
    else:
        perviy = S(x+1, y)
        vtoroy = S(x+2, y)
        res = perviy + vtoroy
        return res

ot2do9 = S(2, 9)
ot9do18 = S(9, 18)
print(ot2do9*ot9do18)"""