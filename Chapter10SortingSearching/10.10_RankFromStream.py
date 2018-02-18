import sys
seenNumbers = dict()


def trackInt(num):
    if(seenNumbers.has_key(num)):
        seenNumbers[num] +=1
    else:
        seenNumbers[num] =1

def getRank(num,upper):
    rank = 0
    for i in range(num,upper):
        if(seenNumbers.has_key(i)):
            rank += seenNumbers[i]
    return rank

inputArr = [5,1,4,4,5,9,7,13,3]

maxInt = 0
for x in inputArr:
    if x > maxInt:
        maxInt = x
    trackInt(x)
    print "rank of {0} is {1}".format(x,getRank(x,maxInt))
