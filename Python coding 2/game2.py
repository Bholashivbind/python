# import random
# Cnumber=random.randrange(1,101)
# userInput=int(input("Enter Your Number:--"))
# if userInput>Cnumber:
#     print("Your guess is too high")
# elif Cnumber>userInput:
#     print("Your guess number is too low")
# else:
#     print("Computer Number",Cnumber)
#     print("Your guess number is equal")


#     scissors rock paper game

# import random
# l=["rock", "scissor", "paper"]
# '''
# rock vs paper-> paper wins
# rock vs scissors-> rock wins
# paper vs scissors-> scissors wins
# '''
# while True:
#     ccount=0
#     ucount=0
#     uc=int(input('''
# Game Start...
# 1 yes
# 2 No | Exit  
#     '''))
#     if uc==1:
#         for a in range(1,6):
#             userInput=int(input('''
# 1 Rock 
# 2 Scissor
# 3 Paper   
#                         '''))
#             if userInput==1:
#                 uchoice="rock"
#             elif userInput==2:
#                 uchoice="scissor"
#             elif userInput==3:
#                 uchoice="paper"
#             Cchoice=random.choice(l)
#             if Cchoice==uchoice:

#                 print("Computer Value",Cchoice)
#                 print("User Value", uchoice)
#                 print("Game Draw")
#                 ucount=ucount+1
#                 ccount=ccount+1
#             elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or(uchoice=="scissor" and Cchoice=="paper"):
#                 print("Computer Value",Cchoice)
#                 print("User Value", uchoice)
#                 print("You Win")
#                 ucount=ucount+1
#             else:
#                 print("Computer Value",Cchoice)
#                 print("User Value", uchoice)
#                 print("Computer Win")
#                 ccount=ccount+1
#         if ucount==ccount:
#             print ("Final Game Draw...")
#             print("User Score",ucount)
#             print("Computer Score",ccount)
#         elif ucount>ccount:
#             print ("Final You win the Game ...")
#             print("User Score",ucount)
#             print("Computer Score",ccount)
#         else:
#             print ("Final Computer win the Game ...")
#             print("User Score",ucount)
#             print("Computer Score",ccount)

#     else:
#         break


#      ***Pickle library***

# import pickle
# l= [10, 20, 30, 40, 50]
# file=open("writedata.txt","wb")
# pickle.dump(l,file)
# file.close()

                
import pickle
file=open("writedata.txt","rb")
l=pickle.load(file)
print(l)

