#List1- List2ss

l1=eval(input("Enter values in list 1:"))
l2=eval(input("Enter values in list 2:"))
def diff_list(l1,l2):
    final=[]
    for x in l1:
        if x not in l2:
            final.append(x)

    print(final)

diff_list(l1,l2)

def diff_set(l1,l2):
    final=list((set(l1)-set(l2)))
    print(final)

diff_set(l1,l2)

