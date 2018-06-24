import time
import sys
sys.setrecursionlimit(1000000)
def product(x, n):
    if n == 0:
        return 0
    else:
        return x + product(x, n-1)

if __name__ == '__main__':
    start = time.time()
    print(product(2,100000))
    stop = time.time()
    print("recursive_product :", stop - start)
    start = time.time()
    print(2*100000)
    stop = time.time()
    print("product :", stop - start)
