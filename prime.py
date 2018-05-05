n=int(input("Enter a number:"))
def prime(n):
    i=2
    while(i<n):
        if(n%i==0):
            print("Not a prime number")
            break
        i=i+1
    else:
        print("Prime Number")

prime(n)
