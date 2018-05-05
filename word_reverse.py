s=input("Enter a string:")
def reverse(s):
    l=s.split()
    s1 = " ".join(l[::-1])
    print(s1)


reverse(s)
