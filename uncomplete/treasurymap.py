row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasury? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical][horizontal] = 'X'
print(map[vertical], map[horizontal])

# for i in range(len(map)):
#     for position in range(len(map[i])):
#         map[i][position] = "X"
#         print(map[i][position], end=" ")

# list1 = [[1, 2, 3], [1, 2, 3]]

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         print(list1[i][j], end=" ")
#     print()
