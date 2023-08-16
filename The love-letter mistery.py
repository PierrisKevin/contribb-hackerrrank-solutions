def theLoveLetterMystery(s):
    res = 0
    ch = list(s)
    for i in range(len(s)):
        if ch[i]!=ch[-(i+1)]:
            maxCh = ord(ch[i]) if ord(ch[i])>ord(ch[-(i+1)]) else ord(ch[-(i+1)])
            res+=abs(ord(ch[i])- ord(ch[-(i+1)]))
            ch[i]=ch[-(i+1)]=chr(maxCh)
    return res

print(theLoveLetterMystery("abc"))