# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max=0
    sumMax=0
    for i in ar:
        if max < i:
            max=i
            sumMax=1
        elif max == i:
            sumMax+=1
    return sumMax
