# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height1= float(height)
weight1=int(weight)

bmi = round(weight1//height1**2)

print(bmi)

