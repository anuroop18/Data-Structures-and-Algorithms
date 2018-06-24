#There is some error in this algorithm

def unique(s, start, stop):
    if start == stop:
        return True
    else:
        if s[start] == s[stop]:
            return False
        #Error area begins.................
        else:
            unique(s, start+1, stop)
            unique(s, start, stop-1)
        return True

if __name__ == '__main__':
    s = [7,9,7,6]
    print(unique(s, 0, len(s)-1))
