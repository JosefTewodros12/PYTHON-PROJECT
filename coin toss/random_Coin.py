import random
import menu

while (True):
    menu.menu_game()
    player_menu = int(input("Please enter your choice: "))
    if (player_menu == 1):
        random_coin = random.randint(0, 1)
        player_choice = input("Please enter your coin side: ").lower()
        if (random_coin == 0):
            computerMove = "head"
        else:
            computerMove = "tail"
        if (computerMove == player_choice):
            print(
                f"computerMove: {computerMove}, playerMove: {player_choice}, Result: You Win!")
        else:
            print(
                f"computerMove: {computerMove}, playerMove: {player_choice}, Result: You Lose")
    elif (player_menu == 2):
        print("Tankyou!")
        break
    else:
        print("Invalid choice")
