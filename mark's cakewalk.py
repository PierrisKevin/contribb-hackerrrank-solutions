def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    return sum([pow(2,i)*calorie[i] for i in range(len(calorie))])