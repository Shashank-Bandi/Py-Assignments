#Printing common elements in both the lists

l1 = eval(input("Enter values in list 1:"))
l2 = eval(input("Enter values in list 2:"))
final=[]

final=[x for x in l1 if x in l2]
print(final)
