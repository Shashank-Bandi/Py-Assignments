#Generating the fibbonaci series
n=int(input("Enter how many numbers to generate:"))
def fib(n):
    i=0
    a=0
    b=1
    while(i<n):
       c=a+b
       a=b
       b=c
       print(c,end=" ")
       i=i+1

fib(n)
