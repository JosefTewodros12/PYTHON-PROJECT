import random
import menu

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

lists = [rock, paper, scissors]

while True:
    menu.game_menu()
    message = int(input("Please choose? "))
    if (message == 1):
        playerChoose = int(input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
        playerMove = lists[playerChoose]

        computer = random.randint(0, 2)
        computerMove = lists[computer]

        if computerMove == playerMove:
            print(
                f"Computer Move: {computerMove}\nPlayer Move: {playerMove} It's a draw")
        elif computerMove == 0 and playerMove == 2:
            print(
                f"Computer Move: {computerMove}\nPlayer Move: {playerMove} You Win")
        elif (computerMove > playerMove):
            print(
                f"Computer Move: {computerMove}\nPlayer Move: {playerMove} You Win")
        else:
            print(
                f"Computer Move: {computerMove}\nPlayer Move: {playerMove} You Lose")
    else:
        print("Thank you!")
        break
