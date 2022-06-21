#f_string

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# days = 365
# weeks = 52
# months = 12
age = int(age)

weeks = (90*52)-(age*52) #total number of weeks till 90 years old

months = (90 * 12) - (age*12) #total number of months till 90 years old

days = (365 * 90)-(age*365) #total number of days till 90 years old

print(f"You have {days} days, {weeks} weeks, and {months} months left")
