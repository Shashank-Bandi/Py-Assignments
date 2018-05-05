import random
print("Note:You will be provided with 5 tries the game will stop automatically once the tries are finished. Please type exit if you want to quit the game :)")
print()
print()
print()

print('''Difficulty Levels:
1.Easy
2.Hard
3.Extreme\n''')
dif=int(input("Select Difficulty Level:"))
if dif==1:
    high=100
    total=10
elif dif==2:
    high=1000
    total=8
else:
    high=5000
    total=5
ans = random.randint(1,high)

print()
print()
n = input("Guess a number between 1 to {}:".format(high))
num=int(n)
c=rem=int()
while True:
 
    if num==(ans):
        print("You`ve guessed it Right!")
        print("Actual number {} ;)".format(ans))
        break
    if num>ans:
        n=input("Guess a lower number:")
        if n.lower()=="exit":
            print("Thanks for playing :)")
            break
        else:
            num=int(n)
            c = c+1
            rem = total-c
            print("Tries Remaining={}".format(rem)) 
    else:
        n=input("Guess a higher number:")
        if n.lower()=="exit":
            print("Thanks for playing :)")
            break
        else:
            num=int(n)
            c = c+1
            rem = total-c
            print("Tries Remaining={}".format(rem)) 

    if rem==0:
        print("You are out of tries:(, Thanks for playing")
        print("Actual number {} ;)".format(ans))
        break

    
