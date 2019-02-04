def is_sorted(sequence):
    if len(sequence)==0 or len(sequence)==1:
        return 1
    startingValue_forInc=sequence[0]
    startingValue_forDec=sequence[0]
    startingValue_forConstant=sequence[0]
    increaseCount=0
    decreaseCount=0
    constantCount=0

    for i,nextValue in enumerate(sequence):
        if i==0:
            continue
        if startingValue_forInc<=sequence[i] and startingValue_forDec>=sequence[i] and startingValue_forConstant==sequence[i]:
            startingValue_forInc=nextValue
            startingValue_forDec=nextValue
            startingValue_forConstant=nextValue
            increaseCount+=1
            decreaseCount+=1
            constantCount+=1
        elif startingValue_forInc<=sequence[i]:
            startingValue_forInc = nextValue
            increaseCount += 1
        elif startingValue_forDec>=sequence[i]:
            startingValue_forDec = nextValue
            decreaseCount += 1
        elif startingValue_forConstant==sequence[i]:
            startingValue_forConstant=nextValue
            constantCount+=1
    if increaseCount==len(sequence)-1:
        return 1
    elif decreaseCount==len(sequence)-1:
        return -1
    elif constantCount==len(sequence)-1:
        return 1
    else:
        return 0
print(is_sorted([5,5,4,3,3,2,1]))
