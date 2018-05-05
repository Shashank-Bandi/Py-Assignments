#Generate a password with difficulty Levels

import random
print(''' Difficulty Level:
1.Easy
2.Medium
3.Hard
4.Quit the program''')
while True:
    diff=int(input("Enter Difficulty you want to enter:"))
    words=['Welcome@123','Hello@123','India@123','Goodday@456']
    an1='1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_-+='
    an2='1234567890abcdefghijklmnopqrstuvwxyz'
    if diff==1:
        print("Your password is {}".format(random.choice(words)))
    elif diff==3:
        password="".join(random.sample(an1,10))
        print("Your password is {}".format(password))
    
    elif diff==2:
        password="".join(random.sample(an2,8))
        print("Your password is {}".format(password))
    elif diff==4:
        print("Thanks for using the password generator program")
        break
