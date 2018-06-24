import time
import sys
sys.setrecursionlimit(1000005)
def linear_sum(s,n):
    if n==0:
        return 0
    else:
        return linear_sum(s, n-1) + s[n-1]

def linear_sum2(s):
    sum = 0
    for value in s:
        sum += value
    return sum

def binary_sum(s, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return s[start]
    else:
        mid = (start+stop)//2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)

if __name__ == '__main__':
    data = [x for x in range(10000)]
    start = time.time()
    print(linear_sum(data, len(data)))
    end = time.time()
    print("time for recursive function : ",end-start)
    start = time.time()
    print(linear_sum2(data))
    end = time.time()
    print("time for iterative function : ",end-start)
    start = time.time()
    print(binary_sum(data, 0, len(data)))
    end = time.time()
    print("time for recursive function(binary recursion) : ",end-start)
