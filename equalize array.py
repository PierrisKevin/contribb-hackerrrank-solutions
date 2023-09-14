from collections import Counter


def equalizeArray(arr):
    counter = dict(Counter(arr))
    sorted_counter = dict(sorted(counter.items(), key=lambda kv: kv[1], reverse=True))
    res = 0
    init = 0
    for i in sorted_counter:
        if init!=0:
            res+=counter[i]
        else:
            init+=1
    return res

arr = [1, 2,3,1,2,3,3,3]
print(equalizeArray(arr))
