def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

if __name__ == '__main__':
    data = sorted([1,2,5,7,19,0,4,5,6,8,23,564,56,78,23,5,78,2,564,45646456456,3445,32231])
    target = int(input("Enter a target integer to search: "))
    search = binary_search(data, target, 0, len(data)-1)
    print(search)
