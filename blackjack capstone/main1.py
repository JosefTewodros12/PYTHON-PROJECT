import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_card = []
computer_card = []


user_card[:] = [random.choice(cards), random.choice(cards)]
computer_card[:] = [random.choice(cards), random.choice(cards)]

sum_user_card = 0
sum_computer_card = 0


if 10 in (user_card and computer_card) and 11 in (user_card and computer_card):
    print(f"Yes detected,computer:{computer_card}user:{user_card}")
else:
    print("Not detected!")

# print(f"user:{user_card}, computer:{computer_card}")
print(f"Your cards: {user_card}")
print(f"Computer's first card: {computer_card[0]}")

for j in computer_card:
    sum_computer_card += j
    if (sum_computer_card < 16):
        computer_card.extend(random.choices(cards))
        # print(computer_card)
        sum_computer_card += j
        if (cards[0] in computer_card):
            if (sum_computer_card > 21):
                cards[0] = 1
                sum_computer_card += cards[1]
            else:
                sum_computer_card += 1
        if (sum_computer_card > 21 and sum_user_card < 21):
            print("user,Win")
            break
            game_over = False
        if (sum_computer_card == 21 and (sum_user_card > 21 or sum_user_card < 21)):
            print("computer,win")
            break
            game_over = False
    else:
        print("More than 16")
        if (cards[0] in computer_card):
            if (sum_computer_card > 21):
                cards[0] = 1
                sum_computer_card += cards[1]
            else:
                sum_computer_card += 1

game_over = True
for i in user_card:
    print(f"computer first card: {computer_card[0]}")
    sum_user_card += j
    if (sum_user_card < 16):
        user_input = input("User, do you want another card? ")
        if user_input == 'y':
            user_card.extend(random.choices(cards))
            sum_user_card += i
        if (sum_user_card > 21 and sum_computer_card < 21):
            print("computer,Win")
            break
            game_over = False
        if (sum_user_card == 21 and (sum_computer_card > 21 or sum_computer_card < 21)):
            print("user,win")
            break
            game_over = False
    elif (cards[0] in user_card):
        if (sum_user_card > 21):
            cards[0] = 1
            sum_user_card += cards[1]
        else:
            sum_user_card += i
    else:
        print(f"The sum of user card is {sum_user_card}")
