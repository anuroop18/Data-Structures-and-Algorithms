from decimal import *
getcontext().prec = 50
a = Decimal(input("Enter a starting integer: "))
b = c = a
m = Decimal(4)
i = Decimal(input("Enter ending integer : "))
result1 = None
result2 = None
result3 = None

while a <= i :
    val1 = a**m
    while b <= i :
        val2 = b**m
        while c <= i :
            val3 = c**m
            val4 = (val1+val2+val3)**Decimal(0.25)
            if (a % Decimal(1) == 0) and (b % Decimal(100) == 0) and (c % Decimal(100) == 0):
                print(a,'  ',b,'  ',c,'  ',val4)
            if val4 % Decimal(1) == 0:
                result1 = a
                result2 = b
                result3 = c
            c+=1
        b+=1
        c=Decimal(1)
    a+=1
    b=Decimal(1)
print(result1)
print(result2)
print(result3)
