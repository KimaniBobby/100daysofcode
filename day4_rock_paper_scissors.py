import random

print ("Welcome to Rock,Paper, Scissors Game!!")
print
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
#Write your code below this line 👇

selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"You have selected, {selection}")

computer_selection = random.randint(0,2)

if selection >=3 or computer_selection <0:
    print("You typed an invalid number,you")

print(f"The computer has selected {computer_selection}")

#User Wins
if selection == 0 and computer_selection == 2:
    print("You win")
    if selection == 2 and computer_selection == 1:
        print("You Win")
        if selection == 1 and computer_selection == 0:
            print("You win")

#Draw situation
if selection == 0 and computer_selection == 0:
    print("You draw")
elif selection == 1 and computer_selection == 1:
     print("You draw")
elif selection == 2 and computer_selection ==2:
    print("You draw")
#Computer wins
if computer_selection == 0 and selection == 2:
    print("The computer wins")
elif computer_selection == 2 and selection == 1:
    print("The computer Wins")
elif computer_selection == 1 and selection == 0:
    print("The Computer wins")    
elif computer_selection == 1 and selection == 0:
    print("The computer wins")




