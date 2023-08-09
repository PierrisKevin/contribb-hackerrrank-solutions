def howManyGames(p, d, m, s):
    res = []
    money = s
    while money>=p:
        res.append(p)
        money-=p
        if p+d>m:
            t = p-d
            if t>m:p=t
            else:p=m 
    if sum(res)>s:return len(res[0:-1])
    return len(res)

p = 16
d = 2
m = 1
s = 9981
print(howManyGames(p,d,m,s))
