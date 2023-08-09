def isPalyndrome(s):return True if s==s[::-1] else False
def palyndrome(s):
    al_combination = []
    for i in range(len(s)):
        letter = list(s)
        letter[i]=""
        al_combination.append(["".join(letter), i])
    res = [i[1] for i in al_combination if isPalyndrome(i[0])]
    if res:return res[0]
    return -1
chaine = "aaab"
print(palyndrome(chaine))
