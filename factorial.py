def factorial1(n):
    if n==0:
        return 1
    else:
        i = 1
        fact = 1
        while i <= n:
            fact *= i
            i+=1
        return fact

def factorial2(n):
    if n==0:
        return 1
    else:
        return n*factorial2(n-1)


if __name__=='__main__':
    n = int(input("Enter a positive integer: "))
    print("factorial1: by loop: ",factorial1(n))
    print("factorial2: by recursion: ",factorial2(n))
