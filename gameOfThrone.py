from itertools import combinations
def isAnagram(s):
    allCombin = combinations(s, 5)
    return list(allCombin)
print(isAnagram("kevin"))
