def reverse(s, start, stop):
    if start < stop-1:
        s[start], s[stop-1] = s[stop-1], s[start]
        return reverse(s, start+1, stop-1)
if __name__ == '__main__':
    s = [1,2,3,4,5,6,7,8,67,56,44,33,12,9]
    reverse(s, 0, len(s))
    print(s)
