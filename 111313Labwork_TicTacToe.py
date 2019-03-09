brd=[0]*9
cp=1
winner=0
moves=0
while winner==0 and moves<9:
    print("Player",cp)
    cell=int(input("Please choose a cell location from 0 to 8?"))
    while cell<0 or cell>8:
        cell=int(input("Please choose a cell?"))
    if brd[cell]!=0:
        print("location occupied")
    else:
        brd[cell]=cp
        if brd[0]==cp and brd[1]==cp and brd[2]==cp:
            winner=cp
        elif brd[3]==cp and brd[4]==cp and brd[5]==cp:
            winner=cp
        elif brd[6]==cp and brd[7]==cp and brd[8]==cp:
            winner=cp
        elif brd[0]==cp and brd[3]==cp and brd[6]==cp:
            winner=cp
        elif brd[1]==cp and brd[4]==cp and brd[7]==cp:
            winner=cp
        elif brd[2]==cp and brd[5]==cp and brd[8]==cp:
            winner=cp
        elif brd[0]==cp and brd[4]==cp and brd[8]==cp:
            winner=cp
        elif brd[2]==cp and brd[4]==cp and brd[6]==cp:
            winner=cp
        if winner==0:
            cp=cp%2+1
        moves+=1
    print(brd[0]," ",brd[1]," ",brd[2])
    print(brd[3]," ",brd[4]," ",brd[5])
    print(brd[6]," ",brd[7]," ",brd[8])
if winner!=0:
    print("Winner is Player ",winner)
else:
    print("It was a draw")
