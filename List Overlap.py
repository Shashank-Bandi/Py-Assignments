#Printing the common elements in the list


l1 = eval(input("Enter a list of values:"))
l2 = eval(input("Enter a list of values:"))
final=[]

for x in l1:
    if x in l2:
        #final.append(x)
        print("{} is common in both lists".format(x))

final = [x for x in l1 if x in l2]
        
print(final)
