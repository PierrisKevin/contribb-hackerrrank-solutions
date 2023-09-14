def beautifulTriplets(d, arr):
    res = []
    for i in range(len(arr)):
        tab = [arr[i]]
        n = i+1
        while len(tab)<3 and n<len(arr):
            if len(tab)<2:
                if arr[n]-arr[i]==d and arr[n] not in tab:tab.append(arr[n])
            elif len(tab)==2:
                if arr[n]-tab[1]==d and arr[n] not in tab:
                    tab.append(arr[n])
            n+=1
        if len(tab)==3:res.append(tab)
    return len(res)

arr = [2,2,3,4,5]
print(beautifulTriplets(1,arr))