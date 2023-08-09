def circularArrayRotation(a, k, queries):
    for i in range(k):
        a = [a[-1]]+a[0:-1]
        print(a)
    return [a[i] for i in queries]

a = [1,2,3]
k = 2
queries = [0,1,2]
circularArrayRotation(a,k,queries)