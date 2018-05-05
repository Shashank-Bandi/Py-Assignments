l = eval(input("Enter list of values:"))
n = int(input("Enter a number to check if the values are less than the entered:"))
final=[]
for x in l:
    if int(x) <n:
        print(" {} is less than {}".format(x,n))
print("list format:")
final = [x for x in l if x<n]
print(final)

