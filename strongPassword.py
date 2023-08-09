def minimumNumber(n, password):
    valid = [False,False,False,False]
    for i in password:
        if i.isdigit():valid[0]=True
        if i.islower():valid[1]=True
        if i.isupper():valid[2]=True
        if i in "!@#$%^&*()-+":valid[3]=True
    if n<6:
        repTst = n + valid.count(False)
        if repTst>=6:return valid.count(False)
        return valid.count(False) + (6-repTst)
    return valid.count(False)

passw = "goxg"
print(minimumNumber(len(passw),passw))