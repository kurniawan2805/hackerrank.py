# Complete the staircase function below.
def staircase(n):
    s=''
    for i in range (n):
        s+='#'
        # print "{0:{1}}".format(n, s)
        print ("{:>{width}}".format(s, width=n))

        #'{:>n}'.format('*')
