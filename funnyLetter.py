def funnyString(s):
    inv = s[::-1]
    inv_val = [abs(ord(inv[i])-ord(inv[i-1])) for i in range(1,len(inv))]
    origin = [abs(ord(s[i])-ord(s[i-1])) for i in range(1,len(inv))]
    if origin==inv_val:return "Funny"
    return "Not Funny"

s = "ivvkx"
print(funnyString(s))