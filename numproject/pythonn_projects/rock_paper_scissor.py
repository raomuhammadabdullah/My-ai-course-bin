"""
wrokfow of project:
1-input from user = rock,paper,scissor
2-computer choice =randome
3-Result print

cases:

A-Rock:
Rock-Rock=tie
Rock-paper=paper win
Rock-scissor=Rock win

2-paper
paper-paper=tie
paper-rock=paper win
paper-scissor=scissor win

3-scissor

scissor-scissor=tie
scissor-rock=rock win
scissor-paper=scissor win

"""
import random
item_list=["rock","paper","scissor"]
user=input("enter your move = Rock,paper,scissor")
computer=random.choice(item_list)
print(f"user choice is = {user}, compter choice = {computer}")
if user==computer:
    print("Both choices are same: = Match is tie")
elif user=="rock":
  if computer=="paper":
     print("paper cover rock = computer  wins ")
  else:
      print("Rock smashes scissior = you win") 
elif user=="paper":
    if computer=="scissor":
       print("scissor cuts paper = computer wins")
    else:
       print("paper covers rock = you win")
elif user=="Scissor":
    if computer=="paper":
      print("scissor cuts paper = you win")    
    else:
       print("Rock mashes scissor = computer wins")        


