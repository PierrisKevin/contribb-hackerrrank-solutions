def isVague(s):
    l = s[1]
    comp = s[0]
    for i in range(1,len(s),2):
        if s[i]!=l or s[i-1]!=comp:return False
    return True 

s = list("asdcbsdcagfsdbgdfanfghbsfdab")
p = list(set(s))
choise = []
for i in range(len(p)):
    for j in range(len(p)):
        if i!=j:
            if not ([p[i],p[j]] in choise or [p[j],p[i]] in choise):choise.append([p[i],p[j]])
resp = []

for i in choise:
    print("".join(s),i[0],i[1])
    ch = "".join(s).replace(i[0],"").replace(i[1],"")
    if len(ch)>3:resp.append(ch)
print(resp)
res = [i for i in resp if isVague(i)]

