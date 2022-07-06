 #🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])

vertical = int(position[1])

selected_row =map[vertical -1]
selected_row[horizontal - 1] = "X"



# if position == "00":
#     map[0] [0]= "X"
# elif position =="01":
#     map[0][1] = "X"
# elif position == "02":
#     map[0][2] = "X"
# elif position == "10":
#     row2[0] = "X"
# elif position == "11":
#     row2[1] = "X"
# elif position == "12":
#     row2[2] = "X"
# elif position == "20":
#     row3[0] = "X"
# elif position == "21":
#     row3[1] = "X"
# elif position == "22":
#     row3[2] = "X"
# else:
#     print("Invalid Input")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")