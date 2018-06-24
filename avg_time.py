from time import time

def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end-start)/n

if __name__ == '__main__':
    print(compute_average(50))
