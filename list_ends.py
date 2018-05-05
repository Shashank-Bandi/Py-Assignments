'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.'''
l=eval(input("Enter list of values:"))
def ends(l):
    size = len(l)
    end = l[:1]+l[size:size-2:-1]
    print(end)
    
ends(l)
