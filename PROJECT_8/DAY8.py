import random
print("         Rock✊  Paper 📄 Scissor ✂️")
print(" ="*25)
print("GAME START")
class RPS_Game :
    def __init__(self,Name,Score,Comp_score) :
        self.Name=Name
        self.Score=Score
        self.comp=Comp_score

Avail_move={"Rock":1,"Paper":2,"Scissor":3}
def Play_Round(n) :
    print(f"----Round {n} Start---")
    Move=int(input("Your's Move (Rock/Paper/Scissor) : "))
    if(Move in Avail_move.values()) :
        Comp_move= random.choice(list(Avail_move.values()))
        print(f"COMPUTER CHOOSE: {Comp_move}")
        if(Move==1 and Comp_move==3) :
            print("You Wins This Round\n")
            Game.Score+=1
        elif(Move==1 and Comp_move==2) :
            print("COMPUTER Wins the Round\n")
            Game.comp+=1
        elif(Move==3 and Comp_move==2) :
            print("You Wins This Round\n")
            Game.Score+=1
        elif(Move==2 and Comp_move==3) :
            print("COMPUTER Wins the Round\n")
            Game.comp+=1
        elif(Move==3 and Comp_move==1  ) :
            print("COMPUTER Wins the Round\n")
            Game.comp+=1
        elif(Move==2 and Comp_move==1  ) :
            print("You Wins This Round\n")
            Game.Score+=1
        else : print("Round Draw")
    else : 
        print("You Choose An Invalid Move")
        print("GAME OVER\n")
        exit()
    return

def Show_score() :
    print("-"*4,end="")
    print("SCOREBORD",end="")
    print("-"*4)
    print(f"{Player_Name} : {Game.Score}")
    print(f"COMPUTER      : {Game.comp}")
    if(Game.Score > Game.comp) : print("You Wins The Match")
    elif(Game.Score == Game.comp) : print("Match Draw")
    else : print("COMPUTER Wins The Match")
    return

Player_Name=input("Enter Player Name: ").strip().title()
Round=int(input("Enter Number Of Rounds: "))
Game=RPS_Game(Player_Name,0,0)  
print("\n")
for i,j in Avail_move.items() :
    print(f"FOR {i} CHOOSE {j}\n")

for i in range(1,Round+1) :
    Play_Round(i)
print("GAME OVER\n")


Show_score()