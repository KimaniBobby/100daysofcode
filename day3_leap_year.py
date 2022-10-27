print("This program determines if a year is a leap year or not")

year = int(input("Which year do you want to check? "))


year4 = year %4 
year100= year % 100
year400 = year %400

if year4 > 0:
    print("Not leap year.")
elif year100 >0:
    print("Leap year.")
elif year400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")


















# **************************************************************
# Alternative Code
# **************************************************************


# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# year4 = year %4 
# year100= year % 100
# year400 = year %400

# if year4 > 0:
#     print("Not leap year.")
# elif year100 >0:
#     print("Leap year.")
# elif year400 == 0:
#     print("Leap year.")
# elif year400 >0:
#     print("Not leap year.")

