import os
from art import logo


def clear_console():
    os.system('cls')


print(logo)


print("Welcome to the secret auction program.")
bids_start = True


def highest_bid():
    max = 0
    for i in bids_list:
        if (i[name] > max):
            max = i[name]
        print(f"The winner is {name} with a bid of ${max}.")


while bids_start:
    bids_list = []
    bids_dic = {}
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    question = input(
        "Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bids_dic[name] = bid
    bids_list.append(bids_dic)
    if (question == 'no'):
        highest_bid()
        bids_start = False
    elif (question == 'yes'):
        clear_console()
