from itertools import combinations
def pairs(k, arr):
    res = []
    allComp = combinations(arr,2)
    for i in allComp:
        diff = abs(i[0]-i[1])
        if diff==k:
            res.append(1)
    return len(res)
k = 2
arr = [1, 5, 3, 4, 2]
print(pairs(k,arr))