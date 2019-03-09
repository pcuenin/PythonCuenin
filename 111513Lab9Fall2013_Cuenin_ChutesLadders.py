import random
#set variables
brd=[0]*100
p1=0
p2=0
winner=0
dice=0
pos=0
#set up the board
cp=1
brd[19]=-10
brd[47]=-15
brd[65]=-20
brd[98]=-50

#set ladders
brd[4]=10
brd[27]=12
brd[63]=20
brd[96]=3

#play game
while winner==0:
    #player ones turn
    if cp==1:
        tmp=input("Player 1 please hit a key and press enter to roll the dice")
        dice=random.randint(1,6)
        print("Player 1 you rolled ",dice)
        pos=dice+p1
        if pos<=99:
            if brd[pos]<0:
                print("player 1 landed on a chute")
            if brd[pos]>0:
                print("player 1 landed on a ladder")
            p1=pos
        else:
            print("Sorry you can not move")
        if p1==99:
            winner=1
            print("Player 1 wins!")
        else:
            cp=2
    #player twos turn
    else:
        tmp=input("Player 2 please hit a key and press enter to roll the dice")
        dice=random.randint(1,6)
        print("Player 2 you rolled ",dice)
        pos=dice+p2
        if pos<=99:
            if brd[pos]<0:
                print("player 2 landed on a chute")
            if brd[pos]>0:
                print("player 2 landed on a ladder")
            p2=pos
        else:
            print("Sorry you can not move")
        if p2==99:
            winner=2
            print("Player 2 wins!")
        else:
            cp=1
    #print the board
    for i in range(99,-1,-1):
        if (i+1)%10==0:
            print("")
        if i==p1 and i==p2:
            print("_12_", end=" ")
        elif i==p1:
            print("_1__", end=" ")
        elif i==p2:
            print("_2__", end=" ")
        else:
            print("____", end=" ")
    print("")
    print("")
print("Thanks for playing!")
            
