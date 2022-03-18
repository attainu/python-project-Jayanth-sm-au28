import random

#boardsize= int(input("Please input board size in multiples of 100"))
boardsize=100

#no_of_dice=int(input("enter no of dices eithre 1 or 2 only"))
no_of_dice=1

#p=int(input("enter number of players"))
#player=list(input("Players names ").split() for x in range(p))
#print(player)
player=['first','second','third','fourth']


#l=int(input("enter number of ladder "))
#ladder=dict(input("enter start and end point of ladder").split() for x in range(l))
#print(ladder)

#s=int(input("enter number of snakes "))
#snake=dict(input("enter start and end point of snake").split() for x in range(s))
#print(snake)

ladder={1:38 ,4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
snake={32:10, 34:6, 48:26, 62:18, 88:24, 95:56, 97:78}



pos=[]

for i in range(len(player)):
    pos.append(0)
print ("Player names are ",player)
print("Initial position of players are ", pos)
print("\n")

def move(player,pos,dice):
    pos2 = pos + dice
    
    if pos2 in snake:
        print(player, "rolled a dice to",dice, "Bitten by snake and moved from ",pos ,"to ",snake[pos2] )
        pos2 = snake[pos2]
        return pos2


    elif pos2 in ladder:
        print(player, "rolled a dice ",dice, " and climbed by ladder and moved from ",pos ,"to ",ladder[pos2])
        pos2 = ladder[pos2]
        return pos2

        
    else:
        if(pos2 > 100):
            print(player, "rolled a dice ",dice, " and moved above ",boardsize," , Please try again in  your next turn")
            return pos
        else:
            print(player, "rolled a dice ",dice, " and moved from ",pos," to ",pos2)
            return pos2

while True:
    for i in range(len(player)):
        input("Hey Player! Press enter  to dice")
        if no_of_dice==1:
            dice = random.randint(1,6)
        elif no_of_dice==2:
             dice = random.randint(2,12)
        else:
            print("Invalid number of dice entered")
        
        pos[i]=move(player[i],pos[i],dice)
        if pos[i] == boardsize:
            print("CONGRTULATIONS! ",player[i]," WON the Game")
            pos.remove(pos[i])
            player.remove(player[i])
            break


    print("Position of ", player," are ",pos," respectively")
    print("\n")