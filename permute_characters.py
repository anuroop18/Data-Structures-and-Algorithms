import time
def puzzle(k, s, u):
    for e in u:
        s.append(e)
        u.remove(e)
        if k==1:
            print(s)
        else:
            puzzle(k-1, s, u)
        s.remove(e)
        u.add(e)

if __name__ == '__main__':
    start = time.time()
    puzzle(5, [], {'a','b','c','d','e'})
    stop = time.time()
    print(stop-start)
