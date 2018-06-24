def maximum(s):
    if len(s)==1:
        return s[0]
    return max(s[len(s)-1],maximum(s[:len(s)-1]))

def minimum(s):
    if len(s) == 1:
        return s[0]
    return min(s[len(s)-1],minimum(s[:len(s)-1]))

if __name__ == '__main__' :
    s = [1,2,4,3,6,0,54,23,556,7,8,5,4]
    print(maximum(s))
    print(minimum(s))
