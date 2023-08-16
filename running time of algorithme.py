def runningTime(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                res+=1
    return res