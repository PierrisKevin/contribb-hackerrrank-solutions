def highestValuePalindrome(s, n, k):
    if n<=1:return "9"
    ch = s
    s = list(map(int,s))
    nb = k
    for i in range(n):
        if s[-(i+1)]!=s[i] and nb>0:
            s[-(i+1)]=s[i]=9
            nb-=1
    s="".join(map(str,s))
    if int(s)>int(ch):
        if s[::-1]==s:return s
        return -1 
    else:
        s = list(map(int,s))
        print("enter to that")
        for i in range(n):
            if nb>0:
                if s[i]<9:
                    s[-(i+1)]=s[i]=9
                    break
        s="".join(map(str,s))
        if s[::-1]==s:return s
        return -1

test = "3943"
print(highestValuePalindrome(test, len(test), 4))