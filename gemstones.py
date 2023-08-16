def gemstones(arr):
    res = set()
    minimum = min([len(i) for i in arr])
    srch = sorted(arr,key=lambda x: len(x))[0]
    for i in range(minimum):
        lt = srch[i][0]
        ch = True
        for j in range(len(arr)):
            if not lt in arr[j]:
                ch=False
                break
        if ch:res.add(lt)
    return len(res)