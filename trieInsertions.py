def trieInsert(n,arr):
    for i in range(n-1):
        indice = i+1
        while arr[indice-1]>arr[indice] and (indice>0 and indice<n):
            arr[indice-1],arr[indice] = arr[indice],arr[indice-1]
            indice-=1
        print(" ".join(map(str,arr)))
arr = [1, 4, 3, 5, 6, 2]
trieInsert(len(arr),arr)