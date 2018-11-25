#source: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max=0
    min=pow(10,9)
    sum=0
    for i in arr:
        sum+=i
        if (min>i):
            min=i
        if (max < i):
            max=i
    print("{} {}".format(sum-max, sum-min))
