def anagram(s):
    millieu = len(s)//2
    s1 = s[0:millieu]
    s2 = s[millieu:len(s)+1]
    if len(s1)!=len(s2):return -1
    res = []
    for i in range(len(s1)):
        indEl = s2.find(s1[i])
        if indEl == -1:
            res.append(s1[i])
        else:
            ch = list(s2)
            ch[indEl]=""
            s2="".join(ch)

    return len(res)

allChaine = ["aaabbb", "ab", "abc", "mnop","xyyx","xaxbbbxx"]
for i in allChaine:
    print(anagram(i))

# print(anagram(s))

# test = "abcd"
# print(test.find("d"))