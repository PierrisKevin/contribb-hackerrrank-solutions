def cutTheSticks(arr):
    res = []
    while len(arr)>0:
        res.append(len(arr))
        minim = min(arr)
        othArr = []
        for i in arr:
            if i-minim>0:othArr.append(i-minim)
        arr = othArr
    return res