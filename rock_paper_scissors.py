import random
play1=input("Enter name of player :")
play2="Computer"
choice=['Rock','Paper','Scissors']
score1 = score2 = int(0)

option=""
while True:
    choice1 = input("{} Select one from Rock/Paper/Scissors:".format(play1))
    choice2 = random.choice(choice)
    if choice1.lower()=="rock" and choice2.lower()=="paper":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play1))
        score1 = score1+1
        print("{} Score:{}".format(play1,score1))
        print("{} Score:{}".format(play2,score2))
    elif choice1.lower()=="scissors" and choice2.lower()=="paper":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play1))
        score1 = score1+1
        print("{} Score:{}".format(play1,score1))
        print("{} Score:{}".format(play2,score2))
    elif choice1.lower()=="paper" and choice2.lower()=="rock":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play1))
        score1 = score1+1
        print("{} Score:{}".format(play1,score1))
        print("{} Score:{}".format(play2,score2))
    elif choice1.lower()=="rock" and choice2.lower()=="scissors":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play1))
        score1 = score1+1
        print("{} Score:{}".format(play1,score1))
        print("{} Score:{}".format(play2,score2))
    elif choice1.lower=="rock" and choice2.lower()=="rock":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("Invalid")    
    elif choice2.lower()=="rock" and choice1.lower()=="paper":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play2))
        score2 = score2+1
        print("{} Score:{}".format(play2,score2))
        print("{} Score:{}".format(play1,score1))
       
    elif choice2.lower()=="scissors" and choice1.lower()=="paper":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play2))
        score2 = score2+1
        print("{} Score:{}".format(play2,score2))
        print("{} Score:{}".format(play1,score1))
    
    elif choice2.lower()=="paper" and choice1.lower()=="rock":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play2))
        score2 = score2+1
        print("{} Score:{}".format(play2,score2))
        print("{} Score:{}".format(play1,score1))
    
    elif choice2.lower()=="rock" and choice1.lower()=="scissors":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("{} Wins".format(play2))
        score1 = score2+1
        print("{} Score:{}".format(play2,score2))
        print("{} Score:{}".format(play1,score1))
    
    elif choice1.lower=="paper" and choice2.lower()=="paper":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("Invalid")
    elif choice1.lower=="scissors" and choice2.lower()=="scissors":
        print("{} chose {} and {} chose {}".format(play1,choice1,play2,choice2))
        print("Invalid")    
    option=input("Do you want to Refresh the score or stop the game or continue?:[R|S|C]:")
    if option.lower() == "r":
        score1=score2=0
        print("Refreshed Scores of {} {} are {} {}".format(play1,play2,score1,score2))
    elif option.lower()=="c":
        continue
    else:
        print("Thanks for playing :)")
        break
    
    
