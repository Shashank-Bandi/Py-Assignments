#Print the divisors of the specified numbers

n = int(input("Enter a number:"))

i=1
while i<=n:
    if n%i==0:
        print("{} is a divisor of {}".format(i,n))
    i=i+1
