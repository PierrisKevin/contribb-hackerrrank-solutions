def twoStrings(s1, s2):
    longer = s1 if len(s1)>len(s2) else s2
    finder = s2 if len(s1)>len(s2) else s1
    res = [i for i in longer if i in finder]
    if res:return "YES"
    return "NO"