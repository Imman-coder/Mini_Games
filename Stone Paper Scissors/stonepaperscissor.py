from os import system
from time import sleep
import random
scoreboard=[0,0]
terms=["","🪨","📄","✂️"]
winning_odds=[0,3,1,2]
possible_hand_movement_chunks=[[["    _______       ","---'   ____)      ","      (_____)     ","      (_____)     ","      (____)      ","---.__(___)       "],[
    "     _______      ","---'    ____)____ ","           ______)","          _______)","         _______) ","---.__________)   "],[
    "    _______       ","---'   ____)____  ","          ______) ","       __________)","      (____)      ","---.__(___)       "]],[[
    "       _______    ","      (____   '---","     (_____)      ","     (_____)      ","      (____)      ","       (___)__.---"],[
    "      _______     "," ____(____    '---","(______           ","(______           "," (_______         ","   (__________.---"],[
    "       _______    ","  ____(____   '---"," (______          ","(__________       ","      (____)      ","       (___)__.---"]]]

def hand_assembly(left_sign,right_sign,spaces=3):
    hand=""
    for x in range(6):
        hand+=possible_hand_movement_chunks[0][left_sign][x]+"\t"+possible_hand_movement_chunks[1][right_sign][x]+"\n"
    return hand


def round_start_anim(round,total_rounds):
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print(hand_assembly(0,0))
    sleep(.2)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\n",hand_assembly(0,0))
    sleep(.15)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\n\n",hand_assembly(0,0))
    sleep(.15)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\n",hand_assembly(0,0))
    sleep(.2)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print(hand_assembly(0,0))
    sleep(.2)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\n",hand_assembly(0,0))
    sleep(.15)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\n\n",hand_assembly(0,0))
    sleep(.15)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\n",hand_assembly(0,0))
    sleep(.2)
    _ = system('cls')
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print(hand_assembly(0,0))
    sleep(.2)
    _ = system('cls')

def roundinfoanimation(user,cpu,round,total_rounds):
    round_start_anim(round,total_rounds)
    result_emote=hand_assembly(user-1,cpu-1)
    print(result_emote)
    if(cpu==user):
        print("Tie")
        return -1
    else:
        if(winning_odds[user]==cpu):
            print("You won!")
            # print("CPU choose "+terms[cpu]+"\nYpu choose",terms[user])
            return 1
        else:
            print("CPU Wins!")
            # print("CPU choose "+terms[cpu]+"\nCpu choose",terms[user])
            return 0



def play(round,total_rounds):
    print("Round ",round,"/",total_rounds,"\t\t You ",scoreboard[1],"\t CPU ",scoreboard[0])
    print("\nList of choices:")
    for x in range(1,4):
        print(x,'.'+terms[x])
    user_input=int(input("Enter your choice[1-3]:"));
    _ = system('cls')
    cpu_input=random.randint(1,3)
    if(user_input>3 or user_input<1):
        print("Invalid input")
        return -1
    else:
        x=roundinfoanimation(user_input,cpu_input,round,total_rounds)
        sleep(2)
        _ = system('cls')
        return x

def display_scoreboard():
    print("Final result:\n You =",scoreboard[1],"\n CPU =",scoreboard[0])

def main():
    _ = system('cls')
    rounds=int(input("Enter no. of rounds:"))
    _ = system('cls')
    if(rounds>0):
        for x in range(1,rounds+1):
            legit_round=0
            while(legit_round==0):
                winner=play(x,rounds)
                if(winner==1): #player wins
                    scoreboard[1]+=1
                    legit_round=1
                    break
                if(winner==0): #cpu wins
                    scoreboard[0]+=1
                    legit_round=1
                    break
        display_scoreboard()


if __name__=="__main__":
    main()
    # print(hand_assembly(1,1))