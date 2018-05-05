num = int(input("Enter a number:"))
check = int(input("Enter another number:"))

if num%4==0:
    print("Multiple of 4")
if num%2==0:
    print("Even Number :)")
else:
    print("Odd Number :)")
if num%check==0:
    print("Divisible :)")
else:
    print("Not Divisible :(")
