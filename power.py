import time
import sys
sys.setrecursionlimit(100000)
def power(x, n):
    if n==0:
        return 1
    else:
        return x*power(x, n-1)


def power1(x, n):
    if n==0:
        return 1
    else:
        partial = power1(x, n//2)
        result = partial*partial
        if n%2 == 1:
            result*=x
        return result

if __name__ == '__main__':
    start = time.time()
    print(power(2,10000))
    end = time.time()
    print("power: ", end-start)
    start = time.time()
    print(power1(2,10000))
    end = time.time()
    print("power1: ", end-start)
