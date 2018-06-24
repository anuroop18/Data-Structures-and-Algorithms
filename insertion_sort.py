def insertion_sort(A):
    """Sort list of comparable order into nondecreasing order"""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j>0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

if __name__ == '__main__':
    A = [1,3,5,7,2,3,4,1,99,1,77]
    print("Real unordered data :",A)
    print("Sorted data :",insertion_sort(A))
