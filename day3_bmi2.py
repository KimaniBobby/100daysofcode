# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# BMI = weight (kg) / height^2(m2)


# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."

weight = float(input("Please enter your current weight in KGS\n"))

height = float(input("Please enter your height in metres squared\n"))

bmi = round(weight / height**2)



# print(type(weight))

# print(type(height))

# print(type(bmi))

if bmi < 18.5 :
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25 :
     print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <30 :
     print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35 :
     print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


