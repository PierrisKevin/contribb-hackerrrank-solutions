from itertools import combinations
def gameOfThrones(s):
    res = []
    data = dict(Counter(s))
    for i in data:
        if data[i]%2!=0:res.append(i)
    if len(res)>1:return "NO"
    return "YES"
print(isAnagram("kevin"))
