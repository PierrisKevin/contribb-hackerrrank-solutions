def beautifulBinaryString(b):
    res = 0
    i = 0
    while i<len(b):
        if b[i:i+3]=="010":
            res+=1
            i=i+2
        i+=1
    return res

print(beautifulBinaryString("0100101010"))