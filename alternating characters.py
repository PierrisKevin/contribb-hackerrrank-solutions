def alternatingCharacters(s):
    res = s[0]
    for i in range(1, len(s)):
        if(s[i]!=res[-1]):
            res+=s[i]
    return len(s)-len(res)

print(alternatingCharacters("BABABA"))