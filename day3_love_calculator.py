# 🚨 Don't change the code below 👇
from pkg_resources import to_filename


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


completelove = (name1+" "+name2).lower()

print(completelove)

totalname = str(sum(map(completelove.count, ['t','r','u','e'])))

totalname2 = str(sum(map(completelove.count, ['l','o','v','e'])))


# totalname2 = sum(map(love2.count, ['t','r','u','e','l','o','v','e']))
totalname3 = totalname + totalname2

# print(totalname)
# print(totalname2)
# print(totalname3)

score = int(totalname3)

if score <10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score} you are alright together")

else:
    print(f"Your score is{score} ")