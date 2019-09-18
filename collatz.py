n = int(input("enter a positive number "))
#the number we will use
while n !=1:
    print(n)
    #checks if a number is odd or even.
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1

print(n)