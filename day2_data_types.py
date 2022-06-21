# print(len("hello"))

# print("Hello"[4])

# int(input("Please enter the value you desire\n"))

# n=734_529.678
# print(type(n)) #type is used to find the kind of data type of a variable.

# print(int(len(645674567)))

#type conversion: change form one data type to another

# num_char = len(input("What is your name\n"))

# new_num_char = str(num_char)

# print("Your name has" " "+ new_num_char+ " " "characters")

# a =float(123)
# print(type(a))
#*********************************************************************
#The purpose of the code is get two digit input and add them together
#*********************************************************************
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Method 1#
#print(type(two_digit_number))
# print(int(two_digit_number[0])+(int(two_digit_number[1])))
#*************************************************************

#Method 2#

num1=int(two_digit_number[0])
num2=int(two_digit_number[1])

print(num1 + num2)


