arr =  list(map(int,"7 4 3 5 6 2".split(" ")))
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
print(arr)
insertion_sort(arr)
print(" ".join(map(str,arr)))