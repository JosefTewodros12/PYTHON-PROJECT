def menu():
    print("################")
    print("MENU")
    print("1.Add some order")
    print("2.Show order")
    print("3.Remove order")
    print("4.Search Food")
    print("5.Exit")
    print("################")


foods = []
while True:
    menu()
    chose = int(input("Enter you choses: "))
    if (chose == 1):
        foods = [x for x in input("Add your orders: ").split()]
    elif (chose == 2):
        for i in range(len(foods)):
            print(foods[i] + " ")
    elif (chose == 3):
        food = input("please enter your foods to delete? ")
        foods.remove(food)
    elif (chose == 4):
        element = input("Please write the foods? ")
        if element in foods:
            print("You order pizza" + element)
        else:
            print("Your food is not in your order list.")
    elif (chose == 5):
        print("Thank you!")
        break
